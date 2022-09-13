
from doctest import DocFileTest


def weight_tweets(df):

    df.loc[df['TweetSentiment_Positive'] > 0, 'TweetSentiment_Positive'] = 0.1 * df['likes'] + df['retweet']

    df.loc[df['TweetSentiment_Negative'] > 0, 'TweetSentiment_Negative'] = 0.1 * df['likes'] + df['retweet']

    df['TweetSentiment_Negative'] = df['TweetSentiment_Negative'].fillna(0)
    df['TweetSentiment_Positive'] = df['TweetSentiment_Positive'].fillna(0)

    mask = (df['likes']+df['retweet'] == 0)

    df.loc[mask,'TweetSentiment_Positive'] = 1
    df.loc[mask,'TweetSentiment_Negative'] = 1

    return df
