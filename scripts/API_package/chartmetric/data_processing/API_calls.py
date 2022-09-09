import requests

def radioplay_API_call(since_date, access_key, artist):

    '''Function returns the daily radio play data in 'json' format'''

    radio_response = requests.get(
        f"https://api.chartmetric.com/api/radio/artist/{artist}/airplays"
        ,headers = {"Authorization":f"Bearer {access_key}"}
        ,params={'since': since_date},).json()

    return radio_response

def spotify_API_call(since_date,until_date,access_key,artist):

    '''Function returns the spotify monthly listener data in
    'json' format'''

    # Non-changing params for API call
    data_source = "spotify"
    field = "listeners"

    # Run API call
    spotify_response = requests.get(
            f"https://api.chartmetric.com/api/artist/{artist}/stat/{data_source}"
            ,headers = {"Authorization":f"Bearer {access_key}"}
            ,params={'since': since_date
                    , 'until': until_date
                    , 'field':field},).json()

    return spotify_response

def instagram_API_call(since_date,until_date
                       ,access_key
                       ,artist):

    '''Function to return the monthly instagram data in 'json' format'''

    domain = 'instagram'
    audienceType = 'followers'
    statsType = 'stat'

    instagram_response = requests.get(
        f"https://api.chartmetric.com/api/artist/{artist}/social-audience-stats"
        ,headers = {"Authorization":f"Bearer {access_key}"}
        ,params={'since': since_date
                , 'until': until_date
                , 'domain': domain
                , 'audienceType':audienceType
                , 'statsType':statsType},).json()

    return instagram_response

def tiktok_API_call(since_date,until_date
                       ,access_key
                       ,artist):

    '''Function to return the monthly tiktok data in 'json' format'''

    domain = 'tiktok'
    audienceType = 'followers'
    statsType = 'stat'

    tiktok_response = requests.get(
        f"https://api.chartmetric.com/api/artist/{artist}/social-audience-stats"
        ,headers = {"Authorization":f"Bearer {access_key}"}
        ,params={'since': since_date
                , 'until': until_date
                , 'domain': domain
                , 'audienceType':audienceType
                , 'statsType':statsType},).json()

    return tiktok_response

def youtube_API_call(since_date,until_date
                       ,access_key
                       ,artist):

    '''Function to return the monthly youtube data in 'json' format'''

    domain = 'youtube'
    audienceType = 'followers'
    statsType = 'stat'

    youtube_response = requests.get(
        f"https://api.chartmetric.com/api/artist/{artist}/social-audience-stats"
        ,headers = {"Authorization":f"Bearer {access_key}"}
        ,params={'since': since_date
                , 'until': until_date
                , 'domain': domain
                , 'audienceType':audienceType
                , 'statsType':statsType},).json()

    return youtube_response
