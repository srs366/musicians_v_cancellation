import pandas as pd
from pandas.api.types import CategoricalDtype

from scripts.Merging_Data.Preprocessing.weighting import weight_tweets


def read_twitter_data(base_url,artist_id,artist_type):

    # Read in the data
    # df = pd.read_csv(f'{base_url}/Tweet_data/{artist_type}/{artist_id}_tweets.csv')

    df = pd.read_csv(f'{base_url}/Tweet_data/Catriona_tweets_scraped/finaldfs/{artist_id}_finaldf.csv')

    return df

def clean_twitter_data(df):

    # Trim the columns

    df_trimmed = df.drop(columns=['Unnamed: 0','Unnamed: 0.1','Text','Username','cleaned_text'
                                  ,'Negative_x','Neutral_x','Positive_x'
                                  ,'Negative_y','Neutral_y','Positive_y'])

    df_trimmed['Datetime'] = pd.to_datetime(df_trimmed['Datetime'],errors='coerce')

    df_trimmed = df_trimmed.dropna()

    # One Hot Encode
    cat_dtype = CategoricalDtype(categories=['Extremely Negative','Negative','Neutral','Positive','Extremely Positive'], ordered=False)

    df_trimmed['classified_sentiment'] = df_trimmed['classified_sentiment'].astype(cat_dtype)
    df_sentiment = pd.get_dummies(data = df_trimmed, columns=["classified_sentiment"],prefix='Sentiment',sparse=False)

    # Group sentiments
    df_sentiment['TweetSentiment_Positive'] = df_sentiment['Sentiment_Positive'] + df_sentiment['Sentiment_Extremely Positive']
    df_sentiment['TweetSentiment_Negative'] = df_sentiment['Sentiment_Negative'] + df_sentiment['Sentiment_Extremely Negative']
    # Some extra cleaning
    twitter_df = df_sentiment.drop(columns=['Sentiment_Extremely Negative'
                                                      ,'Sentiment_Negative'
                                                      ,'Sentiment_Positive'
                                                      ,'Sentiment_Extremely Positive'])

    # twitter_df = weight_tweets(twitter_df)

    # Aggregrate counts
    twitter_df = twitter_df.groupby(by='Datetime').sum()

    return twitter_df
