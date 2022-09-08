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

def merge_spotify_radio(spotify_df, radio_df):

    merged_df = spotify_df.merge(radio_df,how='left',on='date')

    return merged_df
