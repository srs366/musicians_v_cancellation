import seaborn as sns
from matplotlib import pyplot as plt

def generate_chart(df, artist, artist_id, base_url, artist_type, date):

    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(20,15))
    fig.suptitle(f'Charts for {artist}: incident date {date}')

    axes[0].set_title('Spotify monthly listens vs Tweets')
    sns.lineplot(data=df.monthly_listeners, color="b", ax=axes[0])
    ax2 = axes[0].twinx()
    sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax2)
    sns.lineplot(data=df.TweetSentiment_Positive, color="g", ax=ax2)

    axes[1].set_title('Radio monthly plays vs Tweets')
    sns.lineplot(data=df.monthly_spins, color="b", ax=axes[1])
    ax3 = axes[1].twinx()
    sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax3)
    sns.lineplot(data=df.TweetSentiment_Positive, color="g", ax=ax3)

    fig.savefig(f'{base_url}/Exploratory_charts/{artist_type}/{artist_id}.png')
