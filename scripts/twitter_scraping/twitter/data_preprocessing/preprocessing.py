import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from cleantext import clean


from emot.emo_unicode import UNICODE_EMOJI

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
