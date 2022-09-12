from distutils.command.clean import clean
from scripts.Merging_Data.Preprocessing.params import LOCAL_DATA_PATH

from scripts.Merging_Data.Preprocessing.artist_data import read_artist_data
from scripts.Merging_Data.Preprocessing.chartmetric_clean import read_chartmetric_data, clean_chartmetric_data
from scripts.Merging_Data.Preprocessing.twitter_clean import read_twitter_data, clean_twitter_data
from scripts.Merging_Data.Preprocessing.merge_files import merge_dataframes
from scripts.Merging_Data.Charting.make_charts import generate_chart


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

        print(f"running for {artist}")

        chartmetric_data = read_chartmetric_data(base_url=LOCAL_DATA_PATH
                                                 , artist_id=artist_id
                                                 , incident_date=incident_date
                                                 , artist_type=cancelled)

        chartmetric_cleaned = clean_chartmetric_data(chartmetric_data)

        twitter_data = read_twitter_data(base_url=LOCAL_DATA_PATH
                                         , artist_id=artist_id
                                         , artist_type=cancelled)

        twitter_cleaned = clean_twitter_data(twitter_data)

        merged_df = merge_dataframes(chartmetric_df=chartmetric_cleaned
                                     , twitter_df=twitter_cleaned)

        # breakpoint()

        filepath = f"{LOCAL_DATA_PATH}/Merged_data/{cancelled}"

        merged_df.to_csv(f"{filepath}/{artist_id}_merged_data.csv")

        generate_chart(df=merged_df
                       , artist=artist
                       , date=incident_date
                       , artist_id=artist_id
                       , base_url=LOCAL_DATA_PATH
                       , artist_type=cancelled)
