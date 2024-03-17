import getorg
from geopy import Nominatim

geocoder = Nominatim(user_agent="https")
location_dict = {}
location = ""
permalink = ""
title = ""



file = 'marathon.tsv'
with open(file, 'r') as f:
    for idx, line in enumerate(f):
        print(line.split('\t'))
        location, date, time, event = line.split('\t')
        event = event.strip()
        if location[-4:] == ", CA":
            location = location[:-3] + " California"
        
        desc = ' | '.join([location, date, time, event])
        location_dict[desc] = geocoder.geocode(location)
        print('+'*40)
        print(desc, location_dict[desc])
        print(f"""
                <tr>
                    <td>{location}</td>
                    <td>{date}</td>
                    <td>{time}</td>
                    <td>{event}</td>
                </tr>
            """)


m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="./marathon", hashed_usernames=False)

# output the string to update marathon.html


