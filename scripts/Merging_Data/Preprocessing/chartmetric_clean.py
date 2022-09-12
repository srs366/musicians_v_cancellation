import pandas as pd

def read_chartmetric_data(base_url, artist_id, incident_date, artist_type):

    # Read in the data
    df = pd.read_csv(f'{base_url}/API_data/{artist_type}/{artist_id}_chartmetric_{incident_date}.csv')

    return df

def clean_chartmetric_data(df):

    chartmetric_trim = df.drop(columns=['Unnamed: 0','listener_change',
       'spins_change', 'followers_insta', 'av_post_likes_insta',
       'av_post_comments_insta', 'av_post_views_insta',
       'follower_pct_change_insta', 'followers_tiktok', 'av_post_likes_tiktok',
       'av_post_comments_tiktok', 'av_post_views_tiktok',
       'follower_pct_change_tiktok', 'followers_youtube',
       'av_post_likes_youtube', 'av_post_comments_youtube',
       'av_post_views_youtube', 'follower_pct_change_youtube'])

    chartmetric_trim['date'] = pd.to_datetime(chartmetric_trim['date'])

    chartmetric_df = chartmetric_trim.set_index('date')

    return chartmetric_df
