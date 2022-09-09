from twitter.data_preprocessing.artist_data import read_artist_data
from twitter.data_preprocessing.merge import merge_dataframes
from twitter.data_preprocessing.preprocessing import clean_text
from twitter.data_preprocessing.scraping import run_the_tweet
from twitter.data_preprocessing.sentiment import conduct_sentiment_task, get_list_sentiments, get_sentiment_classifications, get_sentiment_scores_df, get_classifications_df
from twitter.data_preprocessing.params import LOCAL_DATA_PATH
import pandas as pd

def setup():
    df = read_artist_data(base_url = f'{LOCAL_DATA_PATH}')

    df_reduced = df[['ARTIST', 'DATE OF CANCELLATION', 'LEVEL OF FAME', 'NICKNAME', 'CANCELLED']]

    return df_reduced

def dataframe_pipeline(df_reduced):

    for artist_id, artist_date, artist_fame, artist_nicknames, artist_is_cancelled in zip in zip(df_reduced['CHARTMETRIC ID'],
                                                                                                   df_reduced['DATE OF CANCELLATION'],
                                                                                                   df_reduced['LEVEL OF FAME'],
                                                                                                   df_reduced['NICKNAME'],
                                                                                                   df_reduced['CANCELLED']):

        artist_tweet_df = run_the_tweet(artist_nicknames, artist_date, 6, artist_fame, 'en')
        artist_tweet_df['cleaned_text'] = artist_tweet_df.Text.apply(clean_text)

        artist_sentiment_scores = get_list_sentiments(artist_tweet_df, conduct_sentiment_task())

        senscores_df = get_sentiment_scores_df(artist_sentiment_scores)
        senclass_df = get_classifications_df(get_sentiment_classifications(artist_sentiment_scores))

        artist_final_df = merge_dataframes(artist_tweet_df, senscores_df, senclass_df)

        artist_final_df.to_csv(f'{LOCAL_DATA_PATH}/{artist_id}_tweets.csv')
        return len(artist_final_df)
