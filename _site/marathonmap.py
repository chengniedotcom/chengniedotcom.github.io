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
        location, date, time, event = line.split('\t')
        if location[-4:] == ", CA":
            location = location[:-3] + " California"
        
        desc = ' | '.join([location, date, time, event])
        location_dict[desc] = geocoder.geocode(location)
        print('+'*40)
        print(desc, location_dict[desc])


m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="./marathonmap", hashed_usernames=False)



