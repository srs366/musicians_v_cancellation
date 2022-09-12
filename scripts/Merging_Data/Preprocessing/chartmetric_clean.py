import pandas as pd

def read_chartmetric_data(base_url, artist_id, incident_date, artist_type):

    # Read in the data
    df = pd.read_csv(f'{base_url}/API_data/{artist_type}/{artist_id}_chartmetric_{incident_date}.csv')

    return df

def clean_chartmetric_data(df):

    chartmetric_trim = df.drop(columns=['Unnamed: 0','listener_change'
                                        ,'spins_change', 'follower_pct_change_insta'
                                        ,'follower_pct_change_tiktok', 'follower_pct_change_youtube'])

    chartmetric_trim['date'] = pd.to_datetime(chartmetric_trim['date'])

    chartmetric_df = chartmetric_trim.set_index('date')

    return chartmetric_df
