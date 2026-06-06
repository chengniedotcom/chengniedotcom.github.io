import io
import sys
_stdout = sys.stdout
sys.stdout = io.StringIO()
import getorg
sys.stdout = _stdout
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError, GeocoderRateLimited
import time
import os
import re
import json

CACHE_FILE = 'geocode_cache.json'

MAJOR_LOCATIONS = {
    'Boston, MA', 'Tokyo, Japan', 'London, UK',
    'Berlin, Germany', 'Chicago, IL', 'New York City, NY',
}

# Map the 2-letter abbreviation found in a TSV location ("City, XX") to the full
# state name used by the USA States Progress map. Foreign races (London, UK /
# Xiamen, China / ...) have no entry here and are simply ignored.
STATE_ABBREV = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
    'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
    'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
    'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
    'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota',
    'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska',
    'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina',
    'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon',
    'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
    'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington',
    'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming',
}


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

def is_major(location):
    return location.strip() in MAJOR_LOCATIONS

geocoder = Nominatim(user_agent="marathon-map-generator", timeout=10)
location_dict = {}
geocode_cache = load_cache()

# Read marathon entries from TSV file
marathon_entries = []
with open('marathon.tsv', 'r') as f:
    for line in f:
        print(line.split('\t'))
        location, date, finish_time, event = line.split('\t')
        event = event.strip()
        finish_time = finish_time.strip()
        if location[-4:] == ", CA":
            location = location[:-3] + " California"

        desc = ' | '.join([location, date, finish_time, event])
        marathon_entries.append((location, date, finish_time, event))

        if location in geocode_cache:
            cached = geocode_cache[location]
            if cached is not None:
                class CachedLocation:
                    def __init__(self, d):
                        self.latitude = d['latitude']
                        self.longitude = d['longitude']
                        self.address = d['address']
                    def __str__(self):
                        return self.address
                location_dict[desc] = CachedLocation(cached)
            else:
                location_dict[desc] = None
            print(f"(cached) {desc} {location_dict[desc]}")
            continue

        max_retries = 5
        for attempt in range(max_retries):
            try:
                result = geocoder.geocode(location)
                location_dict[desc] = result
                geocode_cache[location] = {
                    'latitude': result.latitude,
                    'longitude': result.longitude,
                    'address': result.address,
                } if result else None
                save_cache(geocode_cache)
                print('+'*40)
                print(desc, result)
                time.sleep(1)
                break
            except (GeocoderTimedOut, GeocoderServiceError, GeocoderRateLimited) as e:
                print(f"Geocoding Error for {location}: {str(e)}")
                if attempt < max_retries - 1:
                    wait = (attempt + 1) * 5
                    print(f"Retrying in {wait} seconds...")
                    time.sleep(wait)
                else:
                    print(f"Failed to geocode {location} after {max_retries} attempts")
                    location_dict[desc] = None
                    geocode_cache[location] = None
                    save_cache(geocode_cache)

valid_location_dict = {k: v for k, v in location_dict.items() if v is not None}
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(valid_location_dict, folder_name="./marathon", hashed_usernames=False)


def generate_content(marathon_entries):
    chrono = list(reversed(marathon_entries))  # oldest → newest

    # ── Abbott World Marathon Majors chart ──────────────────────────────────
    majors = [(loc, date, t, evt) for loc, date, t, evt in chrono if is_major(loc)]
    majors_js = json.dumps([
        {'label': [loc.split(',')[0].strip(), date.strip().split()[-1]],
         'time': t}
        for loc, date, t, evt in majors
    ], indent=4)

    # ── All races chart ─────────────────────────────────────────────────────
    all_js = json.dumps([
        {'label': "{} '{}'".format(loc.split(',')[0].strip(), date.strip().split()[-1][2:]),
         'time': t,
         'isMajor': is_major(loc),
         'event': evt}
        for loc, date, t, evt in chrono
    ], indent=4)

    # ── Table rows (newest first = original TSV order) ──────────────────────
    total = len(marathon_entries)
    rows = []
    for i, (loc, date, t, evt) in enumerate(marathon_entries):
        rows.append(f"""    <tr>
        <td>{total - i}</td>
        <td>{loc}</td>
        <td>{date}</td>
        <td>{t}</td>
        <td>{evt}</td>
    </tr>""")
    table_rows = '\n'.join(rows)

    # ── USA States Progress summary ─────────────────────────────────────────
    n_states = len(completed_states(marathon_entries))

    return f"""
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>

<h2 style="margin-top: 40px;">Abbott World Marathon Majors</h2>
<p>My finish times at the Abbott World Marathon Majors, in race order. Orange bar = PR.</p>

<div style="max-width: 660px; margin-bottom: 40px;">
  <canvas id="majorsChart"></canvas>
</div>

<script>
(function() {{
  var majors = {majors_js};

  function toMin(t) {{
    var p = t.split(':').map(Number);
    return p[0] * 60 + p[1] + p[2] / 60;
  }}
  function toHMS(min) {{
    var h = Math.floor(min / 60);
    var m = Math.floor(min % 60);
    return h + ':' + String(m).padStart(2, '0');
  }}

  var mins = majors.map(function(d) {{ return toMin(d.time); }});
  var best = Math.min.apply(null, mins);
  var colors = mins.map(function(m) {{ return m === best ? '#e07b39' : '#4a7fa5'; }});

  new Chart(document.getElementById('majorsChart'), {{
    type: 'bar',
    data: {{
      labels: majors.map(function(d) {{ return d.label; }}),
      datasets: [{{ data: mins, backgroundColor: colors, borderRadius: 4 }}]
    }},
    options: {{
      plugins: {{
        legend: {{ display: false }},
        tooltip: {{ callbacks: {{ label: function(ctx) {{ return '  ' + majors[ctx.dataIndex].time; }} }} }}
      }},
      scales: {{
        y: {{
          min: 155,
          ticks: {{ callback: function(val) {{ return toHMS(val); }}, stepSize: 5 }},
          title: {{ display: true, text: 'Finish time (h:mm)' }}
        }}
      }}
    }}
  }});
}})();
</script>

<h2 style="margin-top: 40px;">All Marathons</h2>
<p>Finish times for all {total} marathons. Orange dots = Abbott World Majors.</p>

<div style="max-width: 800px; margin-bottom: 40px;">
  <canvas id="allRacesChart"></canvas>
</div>

<script>
(function() {{
  var races = {all_js};

  function toMin(t) {{
    var p = t.split(':').map(Number);
    return p[0] * 60 + p[1] + p[2] / 60;
  }}
  function toHMS(min) {{
    var h = Math.floor(min / 60);
    var m = Math.floor(min % 60);
    var s = Math.round((min % 1) * 60);
    return h + ':' + String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
  }}

  var mins = races.map(function(d) {{ return toMin(d.time); }});
  var pointColors = races.map(function(d) {{ return d.isMajor ? '#e07b39' : '#4a7fa5'; }});
  var pointRadius = races.map(function(d) {{ return d.isMajor ? 7 : 5; }});

  new Chart(document.getElementById('allRacesChart'), {{
    type: 'line',
    data: {{
      labels: races.map(function(d) {{ return d.label; }}),
      datasets: [{{
        data: mins,
        borderColor: '#aac4dc',
        borderWidth: 1.5,
        pointBackgroundColor: pointColors,
        pointRadius: pointRadius,
        pointHoverRadius: 9,
        tension: 0.2,
        fill: false,
      }}]
    }},
    options: {{
      plugins: {{
        legend: {{ display: false }},
        tooltip: {{
          callbacks: {{
            title: function(items) {{ return races[items[0].dataIndex].event; }},
            label: function(ctx) {{ return '  ' + races[ctx.dataIndex].time; }}
          }}
        }}
      }},
      scales: {{
        x: {{ ticks: {{ maxRotation: 45, font: {{ size: 11 }} }} }},
        y: {{
          ticks: {{
            callback: function(val) {{
              var h = Math.floor(val / 60);
              var m = Math.floor(val % 60);
              return h + ':' + String(m).padStart(2, '0');
            }}
          }},
          title: {{ display: true, text: 'Finish time (h:mm)' }}
        }}
      }}
    }}
  }});
}})();
</script>

<h2 style="margin-top: 40px;">The full Marathon list</h2>

<table style="width:80%">
    <thead>
        <tr>
            <td>Num</td>
            <td>Location</td>
            <td>Date</td>
            <td>Time</td>
            <td>Event</td>
        </tr>
    </thead>
{table_rows}
</table>

<h2 style="margin-top: 40px;">A map of all the places I have run a full Marathon.</h2>

    <iframe src="/marathon/map.html" height="700" width="850" style="border:none;"></iframe>

<h2 style="margin-top: 40px;">USA States Progress</h2>
<p>Marathons completed in {n_states} of 50 US states. Click a blue state for race details.</p>

    <iframe src="/marathon/us-states-map.html" height="640" width="980" style="border:none; max-width:100%;"></iframe>

"""


# Template for marathon/us-states-map.html. Realistic state geometry is loaded
# at view time from the us-atlas TopoJSON (CDN) and drawn with D3 / Albers-USA;
# we only inject the completed-states data, abbreviations, and progress counters.
# Tokens: __DATA__, __ABBR__, __COUNT__, __TOTAL__, __PERCENT__.
_US_STATES_TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>USA Marathon States Progress</title>
<style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; margin: 0; background: #fff; }
        #map-container { width: 960px; height: 600px; margin: 0 auto; position: relative; background: radial-gradient(ellipse at 50% 40%, #eaf2fb 0%, #d6e6f5 60%, #c3d8ee 100%); border-radius: 10px; overflow: hidden; }
        .state { stroke: #ffffff; stroke-width: 0.8; transition: fill 0.2s ease; cursor: pointer; }
        .state.completed { fill: url(#blueGrad); }
        .state.remaining { fill: #eef1f5; }
        .state.completed:hover { fill: #1f4e8c; }
        .state.remaining:hover { fill: #e0e5ec; }
        #states { filter: drop-shadow(0 3px 4px rgba(40,70,120,0.25)); }
        .lbl { font-size: 9.5px; font-weight: 600; fill: #fff; text-anchor: middle; pointer-events: none; }
        .lbl.dim { fill: #9aa7b6; }
        .stats { position: absolute; bottom: 18px; left: 18px; background: rgba(255,255,255,0.96); border-radius: 10px; padding: 12px 16px; font-size: 13px; color: #333; box-shadow: 0 2px 10px rgba(0,0,0,0.15); width: 230px; }
        .stats strong { font-size: 15px; color: #1f4e8c; }
        .progress-bar { width: 100%; height: 12px; background: #e8e8e8; border-radius: 6px; margin-top: 8px; overflow: hidden; }
        .progress-fill { height: 100%; border-radius: 6px; width: 0%; background: linear-gradient(90deg, #4a90e2, #1f4e8c); transition: width 0.9s ease; }
        .modal { display: none; position: fixed; z-index: 1000; inset: 0; background: rgba(0,0,0,0.5); }
        .modal-content { background: #fff; margin: 12% auto; padding: 22px; border-radius: 10px; width: 440px; max-width: 90%; }
        .modal-header { font-size: 19px; font-weight: 700; margin-bottom: 14px; }
        .close { float: right; font-size: 26px; font-weight: bold; color: #aaa; cursor: pointer; line-height: 1; }
        .close:hover { color: #333; }
        .marathon-table { width: 100%; border-collapse: collapse; font-size: 13px; }
        .marathon-table th, .marathon-table td { padding: 8px; text-align: left; border-bottom: 1px solid #eee; }
        .marathon-table th { background: #f8f9fa; }
        .marathon-table td { color: #555; }
</style></head><body>
    <div id="map-container">
        <svg id="map" viewBox="0 0 960 600">
            <defs><linearGradient id="blueGrad" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#5a9be8"/><stop offset="100%" stop-color="#2c63ad"/>
            </linearGradient></defs>
            <g id="states"></g><g id="labels"></g>
        </svg>
        <div class="stats"><strong>__COUNT__ of __TOTAL__ states</strong> &mdash; __PERCENT__% complete
            <div class="progress-bar"><div class="progress-fill" style="width:__PERCENT__%"></div></div>
        </div>
    </div>
    <div id="stateModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <div id="modalHeader" class="modal-header"></div>
            <div id="modalDetails" class="modal-details"></div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
    <script src="https://cdn.jsdelivr.net/npm/topojson-client@3"></script>
    <script>
        const DATA = __DATA__;
        const ABBR = __ABBR__;
        const done = new Set(Object.keys(DATA));
        const svg = d3.select('#map'), path = d3.geoPath();
        d3.json('https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json').then(us => {
            const fc = topojson.feature(us, us.objects.states);
            path.projection(d3.geoAlbersUsa().fitSize([960, 600], fc));
            d3.select('#states').selectAll('path').data(fc.features).join('path')
                .attr('d', path)
                .attr('class', d => 'state ' + (done.has(d.properties.name) ? 'completed' : 'remaining'))
                .on('click', (e, d) => showState(d.properties.name))
                .append('title').text(d => done.has(d.properties.name) ? d.properties.name + ' ✓' : d.properties.name);
            d3.select('#labels').selectAll('text').data(fc.features).join('text')
                .attr('class', d => 'lbl ' + (done.has(d.properties.name) ? '' : 'dim'))
                .attr('transform', d => { const c = path.centroid(d); return `translate(${c[0]},${c[1]+3})`; })
                .text(d => ABBR[d.properties.name] || '');
        });
        const modal = document.getElementById('stateModal');
        const closeBtn = document.querySelector('.close');
        function showState(name) {
            const races = DATA[name];
            document.getElementById('modalHeader').textContent = name;
            if (races) {
                let h = '<table class="marathon-table"><thead><tr><th>Date</th><th>Location</th><th>Time</th><th>Event</th></tr></thead><tbody>';
                races.forEach(r => { h += `<tr><td>${r.date}</td><td>${r.location}</td><td>${r.time}</td><td>${r.event}</td></tr>`; });
                h += '</tbody></table>';
                document.getElementById('modalDetails').innerHTML = h;
            } else {
                document.getElementById('modalDetails').innerHTML = '<div style="margin-top:10px"><strong>Status:</strong> Not completed yet<br><br><em>A future marathon opportunity!</em></div>';
            }
            modal.style.display = 'block';
        }
        closeBtn.addEventListener('click', () => modal.style.display = 'none');
        window.addEventListener('click', e => { if (e.target === modal) modal.style.display = 'none'; });
    </script>
</body></html>"""


def extract_state(location):
    """Return the full US state name for a TSV location, or None if foreign.

    Locations look like "City, XX" (state abbreviation). The main loop rewrites
    ", CA" to " California" for geocoding, so handle that spelled-out case too.
    """
    location = location.strip()
    if location.endswith(' California'):
        return 'California'
    if ',' in location:
        tail = location.rsplit(',', 1)[1].strip()
        return STATE_ABBREV.get(tail)
    return None


def completed_states(marathon_entries):
    """Map full state name -> list of race dicts (newest first), US states only."""
    states = {}
    for loc, date, t, evt in marathon_entries:
        state = extract_state(loc)
        if state is None:
            continue
        states.setdefault(state, []).append({
            'location': loc.strip(),
            'date': date.strip(),
            'time': t.strip(),
            'event': evt.strip(),
        })
    return states


def generate_us_states_map(marathon_entries):
    """Regenerate marathon/us-states-map.html from the marathon entries."""
    states = completed_states(marathon_entries)
    done = len(states)
    total = 50
    percentage = round(done / total * 100)
    abbr = {full: ab for ab, full in STATE_ABBREV.items()}

    html = _US_STATES_TEMPLATE
    html = html.replace('__DATA__', json.dumps(states, indent=2))
    html = html.replace('__ABBR__', json.dumps(abbr))
    html = html.replace('__COUNT__', str(done))
    html = html.replace('__TOTAL__', str(total))
    html = html.replace('__PERCENT__', str(percentage))

    out_path = os.path.join('marathon', 'us-states-map.html')
    with open(out_path, 'w') as f:
        f.write(html)
    print(f"Successfully updated {out_path}: {done} of {total} states completed.")


def update_marathon_html():
    html_file_path = os.path.join('_pages', 'marathon.html')
    marker = '<!-- GENERATED CONTENT START -->'

    with open(html_file_path, 'r') as f:
        content = f.read()

    split = content.find(marker)
    if split == -1:
        print("ERROR: Could not find generation marker in marathon.html")
        return

    static_part = content[:split + len(marker)]
    updated = static_part + '\n' + generate_content(marathon_entries)

    with open(html_file_path, 'w') as f:
        f.write(updated)

    print(f"Successfully updated {html_file_path} with {len(marathon_entries)} marathon entries.")

generate_us_states_map(marathon_entries)
update_marathon_html()
