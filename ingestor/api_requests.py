
# Maintainer : Arpit Aggarwal
# Date : 2019-08-03

# sample request for reference url http://osrm-1644136849.us-east-1.elb.amazonaws.com/route/v1/driving/77.6281443,12.9299208;77.6377653,12.9232862?overview=false&steps=true

import json
import requests

#config for the request
#TODO(Arpit): move this out of code
api_url_base = 'http://osrm-1644136849.us-east-1.elb.amazonaws.com'
api_version = 'v1'
profile = 'driving'
headers = {'Content-Type': 'application/json'}


#make the base param for the service based on the config
def get_api_url(service):
    url = api_url_base + '/' + service + '/' + api_version + '/' + profile + '/'
    return url

#Gets route info from osrm given source and dest
def get_route_info(lat1, lon1, lat2, lon2):

    api_url = get_api_url('route')
    api_url += lat1 + ',' + lon1 + ';' + lat2 + ',' + lon2
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

#Gets nearest waypoints for give lat lon
def get_nearest_info(lat, lon):

    api_url = get_api_url('nearest')
    api_url += lat + ',' + lon
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

