import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from pandas.api.types import CategoricalDtype


def merge_dataframes(chartmetric_df, twitter_df):

    merged_df = pd.concat([chartmetric_df, twitter_df], axis=1)

    scaler = MinMaxScaler()

    merged_df[['monthly_listeners'
               , 'monthly_spins']] = scaler.fit_transform(merged_df[['monthly_listeners'
                                                                              , 'monthly_spins']])

    return merged_df

def add_release_data(df,artist_id,base_url):

    to_merge = df

    release_data = pd.read_csv(f'{base_url}/Album_TV_dates/{artist_id}_release_info.csv',index_col=0)
    release_data = release_data.drop(columns=['Artist_ID'])

    cat_dtype = CategoricalDtype(categories=['NEW MUSIC RELEASED','TV SHOW APPEARENCE'], ordered=False)

    release_data['release_type'] = release_data['release_type'].astype(cat_dtype)
    release_data = pd.get_dummies(data = release_data, columns=["release_type"],sparse=False)

    release_data.rename(columns={'release_type_NEW MUSIC RELEASED':'New_Music'
                                 , 'release_type_TV SHOW APPEARENCE':'TV_Show'}, inplace=True)

    release_data.index = pd.to_datetime(release_data.index)

    merged_df = pd.merge(left=to_merge,right=release_data,how='left',right_index=True,left_index=True)

    merged_df['New_Music'].fillna(0, inplace=True)
    merged_df['TV_Show'].fillna(0, inplace=True)

    return merged_df
