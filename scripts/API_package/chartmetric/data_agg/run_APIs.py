from chartmetric.data_processing.params import ACCESS_TOKEN

from chartmetric.data_processing.API_calls import spotify_API_call, radioplay_API_call, instagram_API_call, tiktok_API_call, youtube_API_call

def run_all_APIs(since_date, until_date, artist_id, try_number=1):
    # Run all the APIs
    spotify_response = spotify_API_call(since_date = since_date
                                        , until_date= until_date
                                        , access_key=ACCESS_TOKEN
                                        , artist=artist_id, try_number = try_number)

    radio_response = radioplay_API_call(since_date = since_date
                                        , access_key= ACCESS_TOKEN
                                        , artist = artist_id, try_number = try_number)

    insta_response = instagram_API_call(since_date = since_date
                                        , until_date= until_date
                                        , access_key=ACCESS_TOKEN
                                        , artist=artist_id, try_number = try_number)

    tiktok_response = tiktok_API_call(since_date = since_date
                                        , until_date= until_date
                                        , access_key=ACCESS_TOKEN
                                        , artist=artist_id, try_number = try_number)

    youtube_response = youtube_API_call(since_date = since_date
                                        , until_date= until_date
                                        , access_key=ACCESS_TOKEN
                                        , artist=artist_id, try_number = try_number)

    return spotify_response, radio_response, insta_response, tiktok_response, youtube_response
