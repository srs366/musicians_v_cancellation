from scripts.twitter_scraping.twitter.data_preprocessing.artist_data import read_artist_data
from scripts.twitter_scraping.twitter.data_preprocessing.merge import merge_dataframes
from scripts.twitter_scraping.twitter.data_preprocessing.preprocessing import clean_text
from scripts.twitter_scraping.twitter.data_preprocessing.scraping import run_the_tweet
from scripts.twitter_scraping.twitter.data_preprocessing.sentiment import conduct_sentiment_task, get_list_sentiments, get_sentiment_classifications, get_sentiment_scores_df, get_classifications_df
from scripts.twitter_scraping.twitter.data_preprocessing.params import LOCAL_DATA_PATH
import os

def setup():
    df = read_artist_data(base_url = f'{LOCAL_DATA_PATH}')

    df_reduced = df[['ARTIST', 'CHARTMETRIC ID', 'DATE OF CANCELLATION', 'LEVEL FAME', 'NICKNAME']]

    return df_reduced

def dataframe_pipeline(df_reduced):
    for artist_name, artist_id, artist_date, artist_fame, artist_nicknames in zip(df_reduced['ARTIST'],
                                                                                    df_reduced['CHARTMETRIC ID'],
                                                                                    df_reduced['DATE OF CANCELLATION'],
                                                                                    df_reduced['LEVEL FAME'],
                                                                                    df_reduced['NICKNAME']):

        print(f"Running tweets for {artist_name}")
        artist_tweet_df = run_the_tweet(artist_nicknames, artist_date, 6, artist_fame, 'en')

        print(f"Cleaning tweets for {artist_name}")
        artist_tweet_df['cleaned_text'] = artist_tweet_df.Text.apply(clean_text)

        print(f"Assessing sentiment for tweets relating to {artist_name}")
        artist_sentiment_scores = get_list_sentiments(artist_tweet_df, conduct_sentiment_task())

        print(f"Establishing sentiment scores for tweets relating to {artist_name}")
        senscores_df = get_sentiment_scores_df(artist_sentiment_scores)
        senclass_df = get_classifications_df(get_sentiment_classifications(artist_sentiment_scores))

        print(f"Creating a dataframe for tweets relating to {artist_name}")
        artist_final_df = merge_dataframes(artist_tweet_df, senscores_df, senclass_df)

        final_csv_name = f'{artist_id}_tweets.csv'

        full_path = os.path.join(LOCAL_DATA_PATH, final_csv_name)

        artist_final_df.to_csv(full_path)

        print(f"{artist_name} CSV HAS BEEN SAVED")

    # return len(artist_final_df)
