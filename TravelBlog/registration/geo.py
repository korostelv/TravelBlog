import json
from urllib.request import urlopen


def current_location():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    str = (json.load(response)['loc'])
    list = str.split(',')
    current_loc = []
    for i in list:
        current_loc.append(float(i))
    current_loc_json = json.dumps(current_loc)
    return current_loc_json



