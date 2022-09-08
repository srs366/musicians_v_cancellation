from chartmetric.data_processing.API_calls import spotify_API_call, radioplay_API_call
from chartmetric.data_processing.date_calculator import date_calculator
from chartmetric.data_processing.df_generator import spotify_df_generator, radio_df_generator, merge_spotify_radio
from chartmetric.data_processing.artist_data import read_artist_data

from chartmetric.data_processing.params import LOCAL_DATA_PATH
from chartmetric.data_processing.params import ACCESS_TOKEN


def setup():
    """Artist group should equal cancelled or control"""

    df = read_artist_data(base_url = f"{LOCAL_DATA_PATH}")

    df_reduced = df[['ARTIST','CHARTMETRIC ID', 'DATE OF CANCELLATION','CANCELLED']]

    return df_reduced

def dataframe_pipeline(df):
    """Artist group should equal cancelled or control"""

    for artist_id, incident_date, artist, cancelled in zip(df['CHARTMETRIC ID']
                                                , df['DATE OF CANCELLATION']
                                                , df['ARTIST']
                                                , df['CANCELLED']):

        since_date, until_date = date_calculator(incident_date=incident_date
                                                ,n_months=6)

        spotify_response = spotify_API_call(since_date = since_date
                                            , until_date= until_date
                                            , access_key=ACCESS_TOKEN
                                            , artist=artist_id)

        radio_response = radioplay_API_call(since_date = since_date
                                            , access_key= ACCESS_TOKEN
                                            , artist = artist_id)

        spotify_df = spotify_df_generator(spotify_response)

        radio_df = radio_df_generator(radio_response
                                    , until_date=until_date)

        merged_df = merge_spotify_radio(spotify_df=spotify_df
                                        , radio_df=radio_df)

        filepath = f"{LOCAL_DATA_PATH}/API_data/{cancelled}"

        merged_df.to_csv(f"{filepath}/{artist}_incedent_{incident_date}.csv")
