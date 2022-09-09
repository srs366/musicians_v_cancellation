import json
import requests
import time
import random

def radioplay_API_call(since_date, access_key, artist, try_number):

    '''Function returns the daily radio play data in 'json' format'''

    try:
        radio_response = requests.get(
            f"https://api.chartmetric.com/api/radio/artist/{artist}/airplays"
            ,headers = {"Authorization":f"Bearer {access_key}"}
            ,params={'since': since_date},).json()

    except(requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        print("trying radio API again")
        time.sleep(2**try_number + random.random()*0.01)

        return radioplay_API_call(since_date, access_key, artist, try_number+1)

    else:
        return radio_response

def spotify_API_call(since_date,until_date,access_key,artist,try_number):

    '''Function returns the spotify monthly listener data in
    'json' format'''

    # Non-changing params for API call
    data_source = "spotify"
    field = "listeners"

    # Run API call
    try:
        spotify_response = requests.get(
                f"https://api.chartmetric.com/api/artist/{artist}/stat/{data_source}"
                ,headers = {"Authorization":f"Bearer {access_key}"}
                ,params={'since': since_date
                        , 'until': until_date
                        , 'field':field},).json()

    except(requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        print("trying spotify API again")
        time.sleep(2**try_number + random.random()*0.01)

        return spotify_API_call(since_date,until_date,access_key, artist, try_number+1)

    else:
        return spotify_response

def instagram_API_call(since_date,until_date
                       ,access_key
                       ,artist, try_number):

    '''Function to return the monthly instagram data in 'json' format'''

    domain = 'instagram'
    audienceType = 'followers'
    statsType = 'stat'

    try:
        instagram_response = requests.get(
            f"https://api.chartmetric.com/api/artist/{artist}/social-audience-stats"
            ,headers = {"Authorization":f"Bearer {access_key}"}
            ,params={'since': since_date
                    , 'until': until_date
                    , 'domain': domain
                    , 'audienceType':audienceType
                    , 'statsType':statsType},).json()

    except(requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        print("trying instagram API again")
        time.sleep(2**try_number + random.random()*0.01)

        return instagram_API_call(since_date,until_date
                       ,access_key
                       ,artist, try_number+1)

    else:
        return instagram_response

def tiktok_API_call(since_date,until_date
                       ,access_key
                       ,artist, try_number):

    '''Function to return the monthly tiktok data in 'json' format'''

    domain = 'tiktok'
    audienceType = 'followers'
    statsType = 'stat'

    try:
        tiktok_response = requests.get(
            f"https://api.chartmetric.com/api/artist/{artist}/social-audience-stats"
            ,headers = {"Authorization":f"Bearer {access_key}"}
            ,params={'since': since_date
                    , 'until': until_date
                    , 'domain': domain
                    , 'audienceType':audienceType
                    , 'statsType':statsType},).json()

    except(requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        print("trying tiktok API again")
        time.sleep(2**try_number + random.random()*0.01)

        return tiktok_API_call(since_date,until_date
                       ,access_key
                       ,artist, try_number+1)

    else:
        return tiktok_response

def youtube_API_call(since_date,until_date
                       ,access_key
                       ,artist, try_number):

    '''Function to return the monthly youtube data in 'json' format'''

    domain = 'youtube'
    audienceType = 'followers'
    statsType = 'stat'

    try:
        youtube_response = requests.get(
            f"https://api.chartmetric.com/api/artist/{artist}/social-audience-stats"
            ,headers = {"Authorization":f"Bearer {access_key}"}
            ,params={'since': since_date
                    , 'until': until_date
                    , 'domain': domain
                    , 'audienceType':audienceType
                    , 'statsType':statsType},).json()

    except(requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        print("trying youtube API again")
        time.sleep(2**try_number + random.random()*0.01)

        return youtube_API_call(since_date,until_date
                       ,access_key
                       ,artist, try_number+1)

    else:
        return youtube_response
