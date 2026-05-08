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

"""


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

update_marathon_html()
