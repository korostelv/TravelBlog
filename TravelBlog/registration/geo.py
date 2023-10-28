import json
from urllib.request import urlopen
from geopy.geocoders import Nominatim


# from django.apps import apps
# City = apps.get_model('blog', 'City')
# Post = apps.get_model('blog', 'Post')
# user = request.user

geolocator = Nominatim(user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0")
location = geolocator.geocode("Пермь ,Пермский край, Россия")
# print(location)
# print((location.latitude, location.longitude))


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



