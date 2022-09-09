from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import pandas as pd

def conduct_sentiment_task():

    tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
    model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")

    sentiment_task = pipeline("sentiment-analysis", model= model, tokenizer= tokenizer, top_k=3)

    return sentiment_task

def get_list_sentiments(df_cleanedtext, sentiment_task):
    list_dict_sentiments = []
    for tweet in df_cleanedtext.cleaned_tweet:
        sentiment_task_result = sentiment_task(tweet)[0]
        tweet_sentiment = {}
        for label in sentiment_task_result:
            if label['label'] == 'Neutral':
                tweet_sentiment['Neutral'] = label['score']
            elif label['label'] == 'Positive':
                tweet_sentiment['Positive'] = label['score']
            else:
                tweet_sentiment['Negative'] = label['score']
        list_dict_sentiments.append(tweet_sentiment)
    return list_dict_sentiments

def get_sentiment_classifications(list_dict_sentiments):
    sentiment_classifications = []
    for list_sentiment in list_dict_sentiments:
        if (list_sentiment['Positive'] > list_sentiment['Negative']) and (list_sentiment['Positive'] > (list_sentiment['Neutral'] + list_sentiment['Negative'])):
            sentiment_classifications.append('Extremely Positive')
        elif (list_sentiment['Positive'] > list_sentiment['Negative']) and (list_sentiment['Positive'] < (list_sentiment['Neutral'] + list_sentiment['Negative'])):
            sentiment_classifications.append('Positive')
        elif (list_sentiment['Negative'] > list_sentiment['Positive']) and (list_sentiment['Negative'] > (list_sentiment['Neutral'] + list_sentiment['Positive'])):
            sentiment_classifications.append('Extremely Negative')
        elif (list_sentiment['Negative'] > list_sentiment['Positive']) and (list_sentiment['Negative'] < (list_sentiment['Neutral'] + list_sentiment['Negative'])):
            sentiment_classifications.append('Negative')
        else:
            sentiment_classifications.append('Neutral')
    return sentiment_classifications


def get_sentiment_scores_df(list_dict_sentiments):

    sentiment_scores_df = pd.DataFrame.from_dict(list_dict_sentiments)

    return sentiment_scores_df

def get_classifications_df(sentiment_classifications):

    sentiment_classifications_df = pd.DataFrame.from_dict(sentiment_classifications)

    sentiment_classifications_df = sentiment_classifications_df.rename(columns = {0:'classified_sentiment'})

    return sentiment_classifications_df
