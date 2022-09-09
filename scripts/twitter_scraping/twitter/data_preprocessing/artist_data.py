import pandas as pd

def read_artist_data(base_url):

    df = pd.read_csv(f"{base_url}/artist_data.csv")

    df['NICKNAME'] = df['NICKNAME'].apply(lambda x : x.split(", "))
    df['DATE OF CANCELLATION'] = df['DATE OF CANCELLATION'].apply(lambda x: str(x)[0:10])


    return df
