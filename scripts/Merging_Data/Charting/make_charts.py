import seaborn as sns
from matplotlib import pyplot as plt

def generate_chart(df, artist, artist_id, base_url, artist_type, date):

    # fig, axes = plt.subplots(2, 1, sharex=True, figsize=(20,15))
    # fig.suptitle(f'Charts for {artist}: incident date {date}')

    plt.figure(figsize=(20,10))

    ax = sns.lineplot(data=df.monthly_listeners, color="g",)
    sns.lineplot(data=df.monthly_spins, color="b",)
    ax.set_title(f'{artist}: listen data vs tweets')
    ax.legend(['Average monthly Spotify listens', 'Daily radio plays'])


    ax2 = ax.twinx()
    ax2.set(ylim=(0, 60))
    sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax2)


    plt.savefig(f'{base_url}/Exploratory_charts/{artist_type}/{artist_id}.png')

    plt.close()
