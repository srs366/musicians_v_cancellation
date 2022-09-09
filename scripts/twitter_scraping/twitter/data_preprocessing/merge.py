import pandas as pd

def merge_dataframes(cleaned_tweets_df, sentiment_scores_df, sentiment_classifications_df):

    merge_df = pd.merge(cleaned_tweets_df, sentiment_scores_df, right_index=True, left_index=True)
    merge_df = pd.merge(merge_df, sentiment_classifications_df, right_index=True, left_index=True)

    return merge_df
