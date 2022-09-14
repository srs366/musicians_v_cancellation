import seaborn as sns
from matplotlib import pyplot as plt

def generate_chart(df, artist, artist_id, base_url, artist_type, date):

    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(20,15))
    fig.suptitle(f'Charts for {artist}: incident date {date}')

    axes[0].set_title('Spotify monthly listens vs Tweets')
    sns.lineplot(data=df.monthly_listeners, color="g", ax=axes[0])
    sns.lineplot(data=df.monthly_spins, color="b", ax=axes[0])

    ax2 = axes[0].twinx()
    sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax2)
    # sns.lineplot(data=df.TweetSentiment_Positive, color="g", ax=ax2)

    # axes[1].set_title('Radio monthly plays vs Tweets')
    # sns.lineplot(data=df.monthly_spins, color="b", ax=axes[1])
    # ax3 = axes[1].twinx()
    # sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax3)
    # sns.lineplot(data=df.TweetSentiment_Positive, color="g", ax=ax3)

    # axes[2].set_title('Av post views (insta)')
    # sns.lineplot(data=df.av_post_views_insta, color="b", ax=axes[2])
    # # ax4 = axes[1].twinx()
    # # sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax4)

    # axes[3].set_title('Av post views (tiktok)')
    # sns.lineplot(data=df.av_post_views_tiktok, color="b", ax=axes[3])
    # # ax5 = axes[1].twinx()
    # # sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax5)

    # axes[4].set_title('Av post views (youtube)')
    # sns.lineplot(data=df.av_post_views_youtube, color="b", ax=axes[4])
    # # ax6 = axes[1].twinx()
    # # sns.lineplot(data=df.TweetSentiment_Negative, color="r", ax=ax6)

    fig.savefig(f'{base_url}/Exploratory_charts/{artist_type}/{artist_id}.png')

    plt.close()
