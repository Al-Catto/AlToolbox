import sys
import urllib.parse
import requests
from math import radians, cos, sin, asin, sqrt

BASE_URI = "https://www.metaweather.com"
"""Check URL response"""
response = requests.get(BASE_URI)
print(response)


def search_city(query):
    payload = f"https://www.metaweather.com/api/location/search/?query={query}"
    r = requests.get(payload).json()
    if len(r) > 0:
        return r[0]
    else:
        return None  


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r

if __name__ == "__main__":
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 50.765070, 8.480009
    distance = haversine(lon1, lat1, lon2, lat2)
    print(distance)