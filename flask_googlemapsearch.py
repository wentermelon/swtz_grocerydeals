import googlemaps
from datetime import datetime
import json


def flask_googlemapsearch(user_address, user_radius):
    # Note: user_radius will have to be capped at MAYBE <25000? due to weird, inconsistent results
    API_key = "AIzaSyC5hX_ccGsWexNYHYVreA8qsFtG0Kj9MHM"
    gmaps = googlemaps.Client(key=API_key)

    # Location and user generality, but for now rely on user address
    user_lat = gmaps.geocode(user_address)[0]['geometry']['location']['lat']
    user_long = gmaps.geocode(user_address)[0]['geometry']['location']['lng']
    user_latlong = (user_lat, user_long)

    gmaps_nearby = gmaps.places_nearby(
        user_latlong, user_radius, type='grocery_or_supermarket' or 'store' or 'establishment' or 'food')['results']

    if not len(gmaps_nearby):
        print("No results nearby! Try expanding your search radius.")
    # else:
        # print(gmaps_nearby)
        #gmaps_json = json.dumps(gmaps_nearby)
        # print(gmaps_json)

    store_dict = {}
    store_list = ['metro', 'longo\'s', 'zehrs', 'no frills']

    for store in gmaps_nearby:
        if "metros" in store['name'].lower() or "longo's" in store['name'].lower() or "no frills" in store['name'].lower() or "zehrs" in store['name'].lower():
            store_dict[store['name']] = store['vicinity']
    #store_location = store['name'] + " at " + store['vicinity']
    # store_list.append(store_location)

    return store_dict
