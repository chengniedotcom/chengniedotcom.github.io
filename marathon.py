import getorg
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time
import os
import re

# Initialize geocoder with timeout and proper user agent
geocoder = Nominatim(user_agent="marathon-map-generator", timeout=10)
location_dict = {}
location = ""
permalink = ""
title = ""



# Read marathon entries from TSV file
file = 'marathon.tsv'
marathon_entries = []

with open(file, 'r') as f:
    for idx, line in enumerate(f):
        print(line.split('\t'))
        location, date, time, event = line.split('\t')
        event = event.strip()
        # Handle special cases for locations
        if location[-4:] == ", CA":
            location = location[:-3] + " California"
        
        # Additional processing for international locations might be needed here
        
        desc = ' | '.join([location, date, time, event])
        marathon_entries.append((location, date, time, event))
        
        # Attempt geocoding with retry mechanism
        max_retries = 3
        for attempt in range(max_retries):
            try:
                location_dict[desc] = geocoder.geocode(location)
                print('+'*40)
                print(desc, location_dict[desc])
                break  # Break the retry loop if successful
            except (GeocoderTimedOut, GeocoderServiceError) as e:
                print(f"Geocoding Error for {location}: {str(e)}")
                if attempt < max_retries - 1:  # Don't sleep on the last attempt
                    print(f"Retrying in {(attempt+1)*2} seconds...")
                    time.sleep((attempt+1) * 2)  # Exponential backoff
                else:
                    print(f"Failed to geocode {location} after {max_retries} attempts")
                    # Use None for failed geocoding to avoid breaking the script
                    location_dict[desc] = None
        # print(f"""
        #         <tr>
        #             <td>{location}</td>
        #             <td>{date}</td>
        #             <td>{time}</td>
        #             <td>{event}</td>
        #         </tr>
        #     """)


# Filter out any failed geocoding entries (locations that returned None)
valid_location_dict = {k: v for k, v in location_dict.items() if v is not None}

# Create and output the map with valid locations
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(valid_location_dict, folder_name="./marathon", hashed_usernames=False)

# Update the marathon.html file
def update_marathon_html():
    html_file_path = os.path.join('_pages', 'marathon.html')
    
    # Read the current content of marathon.html
    with open(html_file_path, 'r') as file:
        content = file.read()
    
    # Extract the header part (everything before the table entries)
    header_match = re.search(r'(.*?<thead>\s*<tr>\s*<td>Num</td>\s*<td>Location</td>\s*<td>Date</td>\s*<td>Time</td>\s*<td>Event</td>\s*</tr>\s*</thead>)', content, re.DOTALL)
    if not header_match:
        print("Error: Could not find the table header in marathon.html")
        return
    
    header = header_match.group(1)
    
    # Generate the table rows
    table_rows = []
    total_entries = len(marathon_entries)
    
    for i, (location, date, time, event) in enumerate(marathon_entries):
        row_num = total_entries - i  # Reverse numbering (newest = highest number)
        table_row = f'''
    <tr>
        <td>{row_num}</td>
        <td>{location}</td>
        <td>{date}</td>
        <td>{time}</td>
        <td>{event}</td>
    </tr>'''
        table_rows.append(table_row)
    
    # Combine the header and table rows to form the updated content
    updated_content = header + ''.join(table_rows) + '''
</table>
'''
    
    # Write the updated content back to marathon.html
    with open(html_file_path, 'w') as file:
        file.write(updated_content)
    
    print(f"Successfully updated {html_file_path} with {total_entries} marathon entries.")

# Call the function to update marathon.html
update_marathon_html()


