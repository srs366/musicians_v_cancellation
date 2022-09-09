import re
import string
import nltk
import emoji
from cleantext import clean

def clean_text(tweet):
    #changing to lowercase
    tweet = tweet.lower()

    # removing #´s
    tweet = re.sub(r'#[A-Za-z0-9]+', '', tweet)
    tweet = re.sub(r'#', '', tweet)

    #remove RT
    tweet = re.sub(r'RT[\s]+', '', tweet)

    #remove links
    tweet = re.sub(r'https?:\/\/\S+', '', tweet)
    tweet = re.sub(r"www.\S+", "", tweet)

    #remove indentation
    tweet = re.sub(r'\n', '', tweet)

    #remove emojis
    cleaned_tweet = clean(tweet, no_emoji=True)

    return cleaned_tweet
