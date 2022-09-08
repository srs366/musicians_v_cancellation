import pandas as pd
import datetime

def spotify_df_generator(spotify_response):

    spotify_dict = {'date':[]
                    ,'monthly_listeners':[]
                    ,'listener_change':[]}

    for response in spotify_response['obj']['listeners']:
        spotify_dict['date'].append(response['timestp'][0:10])
        spotify_dict['monthly_listeners'].append(response['value'])
        spotify_dict['listener_change'].append(response['diff'])

    # Turn dictionary into dateframe
    spotify_df = pd.DataFrame.from_dict(spotify_dict)
    # Create %-change column based on monthly listeners (compared to previous day)
    spotify_df['listener_pct_change'] = spotify_df['monthly_listeners'].pct_change(periods=1)
    # Convert date column to datetime
    spotify_df['date'] = pd.to_datetime(spotify_df['date'])
    # Convert NAs to 0's
    spotify_df = spotify_df.fillna(0)

    return spotify_df

def radio_df_generator(radio_response, until_date):

    radio_dict = {'date':[]
                  ,'monthly_spins':[]}

    for response in radio_response['obj']:
        radio_dict['date'].append(response['air_date'])
        radio_dict['monthly_spins'].append(response['spins'])

    # Turn dictionary into dataframe
    radio_df = pd.DataFrame.from_dict(radio_dict)

    # Calculate numeric difference in spins compared to previous day
    radio_df['spins_change'] = radio_df['monthly_spins'].diff(periods=1)
    # Calculate %-change (compared to previous day's spins)
    radio_df['spins_pct_change'] = radio_df['monthly_spins'].pct_change(periods=1)

    # Convert unix epoch from milliseconds to seconds
    radio_df['date'] = radio_df['date'].apply(lambda x: x/1000)
    # Go from unix epoch to datetime
    radio_df['date'] = radio_df['date'].apply(lambda x: datetime.datetime.fromtimestamp(x).date())
    # Convert date column to datetime
    radio_df['date'] = pd.to_datetime(radio_df['date'])
    # Remove dates after the specified 'until_date'
    radio_df = radio_df[radio_df['date'] <= until_date]

    # Converts NAs to 0's
    radio_df = radio_df.fillna(0)

    return radio_df

def tiktok_df_generator(tiktok_response):
    tiktok_dict = {'date':[]
                  ,'followers_tiktok':[]
                  ,'av_post_likes_tiktok':[]
                  ,'av_post_comments_tiktok':[]
                  ,'av_post_views_tiktok':[]}

    for response in tiktok_response['obj']:
        tiktok_dict['date'].append(response['timestp'][0:10])
        tiktok_dict['followers_tiktok'].append(response['followers'])
        tiktok_dict['av_post_likes_tiktok'].append(response['avg_likes_per_post'])
        tiktok_dict['av_post_comments_tiktok'].append(response['avg_comments_per_post'])
        tiktok_dict['av_post_views_tiktok'].append(response['avg_views_per_post'])


    # Turn dictionary into dateframe
    tiktok_df = pd.DataFrame.from_dict(tiktok_dict)
    # Create %-change column based on monthly listeners (compared to previous day)
    tiktok_df['follower_pct_change_tiktok'] = tiktok_df['followers_tiktok'].pct_change(periods=1)
    # Convert date column to datetime
    tiktok_df['date'] = pd.to_datetime(tiktok_df['date'])
    # Convert NAs to 0's
    tiktok_df = tiktok_df.fillna(0)

    return tiktok_df

def insta_df_generator(insta_response):
    insta_dict = {'date':[]
                  ,'followers_insta':[]
                  ,'av_post_likes_insta':[]
                  ,'av_post_comments_insta':[]
                  ,'av_post_views_insta':[]}

    for response in insta_response['obj']:
        insta_dict['date'].append(response['timestp'][0:10])
        insta_dict['followers_insta'].append(response['followers'])
        insta_dict['av_post_likes_insta'].append(response['avg_likes_per_post'])
        insta_dict['av_post_comments_insta'].append(response['avg_comments_per_post'])
        insta_dict['av_post_views_insta'].append(response['avg_views_per_post'])


    # Turn dictionary into dateframe
    insta_df = pd.DataFrame.from_dict(insta_dict)
    # Create %-change column based on monthly listeners (compared to previous day)
    insta_df['follower_pct_change_insta'] = insta_df['followers_insta'].pct_change(periods=1)
    # Convert date column to datetime
    insta_df['date'] = pd.to_datetime(insta_df['date'])
    # Convert NAs to 0's
    insta_df = insta_df.fillna(0)

    return insta_df

def merge_spotify_radio(spotify_df, radio_df, insta_df, tiktok_df, artist_id):

    merged_df = spotify_df.merge(radio_df,how='left',on='date')

    merged_df = merged_df.merge(insta_df,how='left',on='date')
    merged_df = merged_df.merge(tiktok_df,how='left',on='date')

    merged_df['Artist_ID'] = artist_id

    return merged_df
