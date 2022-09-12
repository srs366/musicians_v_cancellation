import seaborn as sns
from matplotlib import pyplot as plt

def generate_chart(df, artist, artist_id, base_url, artist_type, date):

    fig, axes = plt.subplots(5, 1, sharex=True, figsize=(30,15))
    fig.suptitle(f'Charts for {artist}: incident date {date}')

    axes[0].set_title('Spotify monthly listens vs Tweets')
    sns.lineplot(data=df.monthly_listeners, color="b", ax=axes[0])
    ax2 = axes[0].twinx()
    sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax2)
    # sns.lineplot(data=df.TweetSentiment_Positive, color="g", ax=ax2)

    axes[1].set_title('Radio monthly plays vs Tweets')
    sns.lineplot(data=df.monthly_spins, color="b", ax=axes[1])
    ax3 = axes[1].twinx()
    sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax3)
    # sns.lineplot(data=df.TweetSentiment_Positive, color="g", ax=ax3)

    axes[2].set_title('Followers (insta) vs Tweets')
    sns.lineplot(data=df.followers_insta, color="b", ax=axes[2])
    ax4 = axes[1].twinx()
    sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax4)

    axes[3].set_title('Av post likes (insta) vs Tweets')
    sns.lineplot(data=df.av_post_likes_insta, color="b", ax=axes[3])
    ax5 = axes[1].twinx()
    sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax5)

    axes[4].set_title('Av post comments (insta) vs Tweets')
    sns.lineplot(data=df.av_post_comments_insta, color="b", ax=axes[4])
    ax6 = axes[1].twinx()
    sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax6)

    fig.savefig(f'{base_url}/Exploratory_charts/{artist_type}/{artist_id}.png')

    plt.close()
