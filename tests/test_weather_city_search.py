from AlToolbox.weather_city_search import search_city

def test_search_city():
    assert(search_city('london').get('title')) == 'London'