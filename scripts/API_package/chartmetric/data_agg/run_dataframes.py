from chartmetric.data_processing.df_generator import insta_df_generator, spotify_df_generator, radio_df_generator, tiktok_df_generator, youtube_df_generator

def run_all_dataframes(spotify_response
                       , radio_response
                       , insta_response
                       , tiktok_response
                       , youtube_response
                       , until_date):

    spotify_df = spotify_df_generator(spotify_response)

    radio_df = radio_df_generator(radio_response
                                , until_date=until_date)

    insta_df = insta_df_generator(insta_response)

    tiktok_df = tiktok_df_generator(tiktok_response)

    youtube_df = youtube_df_generator(youtube_response)

    return spotify_df, radio_df, insta_df, tiktok_df, youtube_df
