import snscrape.modules.twitter as sntwitter
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd


def run_the_tweet(keywords,incident_date, n_months, level_fame, language):
    date_format = '%Y-%m-%d'
    dtObj = datetime.strptime(incident_date, date_format)

    if level_fame == 'Legendary':
        min_retweets = 10
    elif level_fame == 'Superstar':
        min_retweets = 10
    elif level_fame == 'Mainstream':
        min_retweets = 2
    else:
        min_retweets = 0

    since_date = (dtObj - relativedelta(months=n_months)).date()

    until_date = since_date + timedelta(days=1)
    final_date = (dtObj + relativedelta(months=n_months)).date()

    n_days = (final_date-since_date).days

    query = " OR ".join(keywords)
    if len(keywords) == 1:
        query = keywords[0]
    tweets_list= []
    for x in range(n_days): #no. of days
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{query} since:{since_date.strftime(date_format)} until:{until_date.strftime(date_format)}  min_retweets:{min_retweets} lang:{language}').get_items()):
            if i > 50: #no. of output tweet
                break
            else:
                tweets_list.append([tweet.date, tweet.retweetCount, tweet.likeCount, tweet.content, tweet.user.username]) #append if statement satisfy
        if x < n_days : # no. of days you want to be return
            since_date = since_date + timedelta(days=1) #add another day
            until_date = until_date + timedelta(days=1) #add another day
        else:
            break
    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime',"retweet","likes", 'Text', 'Username'])
    tweets_df['Datetime'] = tweets_df['Datetime'].apply(lambda x: str(x)[0:10])

    return tweets_df
