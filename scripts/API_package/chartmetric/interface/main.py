from chartmetric.data_agg.run_APIs import run_all_APIs
from chartmetric.data_agg.run_dataframes import run_all_dataframes
from chartmetric.data_processing.date_calculator import date_calculator
from chartmetric.data_processing.df_generator import merge_dataframes
from chartmetric.data_processing.artist_data import read_artist_data

from chartmetric.data_processing.params import LOCAL_DATA_PATH

def setup():
    """Artist group should equal cancelled or control"""

    df = read_artist_data(base_url = f"{LOCAL_DATA_PATH}")

    df_reduced = df[['ARTIST','CHARTMETRIC ID', 'DATE OF CANCELLATION','CANCELLED']]

    return df_reduced

def dataframe_pipeline(df):
    """Artist group should equal cancelled or control"""

    # Loop over each artist from the artist csv
    for artist_id, incident_date, artist, cancelled in zip(df['CHARTMETRIC ID']
                                                , df['DATE OF CANCELLATION']
                                                , df['ARTIST']
                                                , df['CANCELLED']):

        # Calculate date range based on incident date
        since_date, until_date = date_calculator(incident_date=incident_date
                                                ,n_months=6)

        # Run all the APIs
        spotify_response, radio_response, insta_response, tiktok_response, youtube_response = run_all_APIs(since_date=since_date
                                                                                                           ,until_date=until_date
                                                                                                           ,artist_id=artist)
        # Run all the individual dataframes

        spotify_df, radio_df, insta_df, tiktok_df, youtube_df = run_all_dataframes(spotify_response=spotify_response
                                                                                   , radio_response=radio_response
                                                                                   , insta_response=insta_response
                                                                                   , tiktok_response=tiktok_response
                                                                                   , youtube_response=youtube_response
                                                                                   , until_date=until_date)

        # Merge all the dataframes
        merged_df = merge_dataframes(spotify_df=spotify_df
                                        , radio_df=radio_df
                                        , insta_df=insta_df
                                        , tiktok_df=tiktok_df
                                        , youtube_df=youtube_df
                                        , artist_id=artist_id)

        # Save out the dataframes
        filepath = f"{LOCAL_DATA_PATH}/API_data/{cancelled}"

        merged_df.to_csv(f"{filepath}/{artist}_incedent_{incident_date}.csv")
