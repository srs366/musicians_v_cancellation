import pandas as pd

def merge_dataframes(chartmetric_df, twitter_df):

    merged_df = pd.concat([chartmetric_df, twitter_df], axis=1)

    return merged_df
