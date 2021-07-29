import sys
import urllib.parse
import requests

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


from mlproject.distance import haversine

if __name__ == "__main__":
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 50.765070, 8.480009
    distance = haversine(lon1, lat1, lon2, lat2)
    print(distance)