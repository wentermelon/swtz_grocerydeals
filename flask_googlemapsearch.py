import googlemaps
from datetime import datetime
import json

def flask_googlemapsearch(user_address, user_radius):

    API_key = "AIzaSyC5hX_ccGsWexNYHYVreA8qsFtG0Kj9MHM"
    gmaps = googlemaps.Client(key = API_key)

    #Location and user generality, but for now rely on user address
    user_lat = gmaps.geocode(user_address)[0]['geometry']['location']['lat']
    user_long = gmaps.geocode(user_address)[0]['geometry']['location']['lng']
    user_latlong = (user_lat,user_long)

    gmaps_nearby = gmaps.places_nearby(user_latlong,user_radius,type="grocery_or_supermarket")['results']

    if not len(gmaps_nearby):
        print("No results nearby! Try expanding your search radius.")
    else:
        return json.dumps(gmaps_nearby)
