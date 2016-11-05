#!/usr/bin/python2.7
import twitter
from geopy.geocoders import Nominatim

api = twitter.Api(consumer_key='Oq3Ik7pKnm6W7zcOHO2GWUbH4',
                  consumer_secret='dsqBL0XeSHZZJC4Bio8vGzaEno8YI9BQn9ycttbf5h7sPjRXMr',
                  access_token_key='129672567-e9BWIfYmd7mabByt1YqRkZHEhJVluYQvxFOVORI7',
                  access_token_secret='RkPnKgvwM0owNqsqyww09So16y7lkcMUuSQAmZ0BIgnKI')
geolocator = Nominatim()

def query_tweets(latitude, longitude, keyword):
    ''' Get tweets given the location and keyword '''
    geocode = 'geocode=' + latitude + ',' + longitude + ',' + '5mi'
    query = 'q=' + keyword
    api_res = api.GetSearch(
            raw_query = query + '&lang=en&result_type=recent&count=100&'\
                      + geocode)
    res = []
    for r in api_res:
        res.append(r.text)

    return res

def query_lgbt_tweets(latitude, longitude):
    res = []
    res += query_tweets(latitude, longitude, 'lgbt')
    res += query_tweets(latitude, longitude, 'gay')
    res += query_tweets(latitude, longitude, 'lesbian')
    res += query_tweets(latitude, longitude, 'bisexual')
    res += query_tweets(latitude, longitude, 'transgender')
    return res

def get_location_from_addr(addr):
    location = geolocator.geocode(addr)
    return str(location.latitude), str(location.longitude)

# Example:
# location = get_location_from_addr('Canary Wharf')
# print(query_lgbt_tweets(location[0], location[1]))
