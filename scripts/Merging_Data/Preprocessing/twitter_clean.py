import pandas as pd
from pandas.api.types import CategoricalDtype


def read_twitter_data(base_url,artist_id,artist_type):

    # Read in the data
    df = pd.read_csv(f'{base_url}/Tweet_data/{artist_type}/{artist_id}_tweets.csv')

    return df

def clean_twitter_data(df):

    # Trime the columns

    # breakpoint()

    df_trimmed = df.drop(columns=['Unnamed: 0','Text','Username','cleaned_text','Negative','Neutral','Positive'])
    df_trimmed['Datetime'] = pd.to_datetime(df_trimmed['Datetime'],errors='coerce')

    df_trimmed = df_trimmed.dropna()

    # One Hot Encode
    cat_dtype = CategoricalDtype(categories=['Extremely Negative','Negative','Neutral','Positive','Extremely Positive'], ordered=False)

    # breakpoint()

    df_trimmed['classified_sentiment'] = df_trimmed['classified_sentiment'].astype(cat_dtype)
    df_sentiment = pd.get_dummies(data = df_trimmed, columns=["classified_sentiment"],prefix='Sentiment',sparse=False)

    df_trimmed = df.drop(columns=['Unnamed: 0','Text','Username','cleaned_text'])


    # Group sentiments
    df_sentiment['TweetSentiment_Positive'] = df_sentiment['Sentiment_Positive'] + df_sentiment['Sentiment_Extremely Positive']
    df_sentiment['TweetSentiment_Negative'] = df_sentiment['Sentiment_Negative'] + df_sentiment['Sentiment_Extremely Negative']
    # Some extra cleaning
    sentiment_df_cleaned = df_sentiment.drop(columns=['retweet','likes'
                                                      ,'Sentiment_Extremely Negative'
                                                      ,'Sentiment_Negative'
                                                      ,'Sentiment_Positive'
                                                      ,'Sentiment_Extremely Positive'])

    # Aggregrate counts
    twitter_df = sentiment_df_cleaned.groupby(by='Datetime').sum()

    return twitter_df
