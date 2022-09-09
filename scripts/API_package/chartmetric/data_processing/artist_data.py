import pandas as pd

def read_artist_data(base_url):

    df = pd.read_csv(f"{base_url}/artist_data.csv")

    return df
