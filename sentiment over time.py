import pandas as pd
import random
import praw
from datetime import datetime
import statistics
import nltk
from nltk.tokenize import word_tokenize
import plotly.express as px

r = praw.Reddit(
    client_id="0GFgVgByJ065sadDY62Q4g",
    client_secret="KfE32h3JMcZPLSF3UmYMJMsJbrXcaQ",
    password="ftu8uac9edb_TKM1yua",
    user_agent="testscript_for_WSB",
    username="ds105_WSB",
)
def stock_comment_sentiment(comment_list):
    comment_sentiment = list()
    affin=open('AFINN_english.txt')
    sentimentScores={}

    for line in affin:
	    term, score = line.split("\t")
	    sentimentScores[term] = float(score)

    for comment in comment_list:
        words = word_tokenize(comment)
        score=0
        for word in words:
            try:
                score += sentimentScores[word]
            except:
                pass
        comment_sentiment.append(score)
    return sum(comment_sentiment)


comments_df = pd.read_pickle('WSB_Comments.pickle')
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

def stock_comments(ticker):
    global comments_df
    stock_comments_list = dict()
    for comment in comments_df.itertuples():
        key = comment.post_id
        if contains_word(comment.body, ticker):
            if key not in stock_comments_list.keys():
                stock_comments_list[key] = [comment.body]
            else:
                stock_comments_list[key].append(comment.body)
    new_list = dict()
    for key in stock_comments_list:
        print(key)
        sub = r.submission(id=key[3:])
        date_created = sub.created_utc
        date_created=datetime.fromtimestamp(date_created)
        new_list[date_created] = stock_comments_list[key]

    comments_dict = new_list
    sentiments_dict = dict()
    col_1 = []
    col_2 = []
    for dates in comments_dict:
        sentiment = stock_comment_sentiment(comments_dict[dates])
        print(sentiment)
        col_1.append(dates)
        col_2.append(sentiment)

    sentiments_dict['Date'] = col_1
    sentiments_dict['Sentiment'] = col_2

    new_comments_df = pd.DataFrame.from_dict(sentiments_dict)
    #new_comments_df.to_pickle(f'{ticker}_cumul_sentiments.pickle')
    #new_comments_df.to_csv(rf'{ticker}_cumul_sentiments.csv', mode='w')

    fig = px.line(new_comments_df, x="Date", y="Sentiment", title=f"{ticker}")
    # fig.write_image(f"/Users/williamsong/PycharmProjects/pythonProject/{ticker}_sentiment.jpeg")
    # fig.to_image(format="jpeg", width=2560, height=1440, scale=3, engine="kaleido")
    fig.show()


stock_comments('GME')
stock_comments('AMC')
stock_comments('PLTR')
# stock_comments('YOU')
stock_comments('NOK')
# stock_comments('SNDL')
# stock_comments('WISH')
# stock_comments('TSLA')
# stock_comments('CLOV')
# stock_comments('MVIS')
# stock_comments('CLNE')
# # stock_comments('FOR')
# stock_comments('TLRY')
# # stock_comments('ALL')
# # stock_comments('ALL')
# # stock_comments('GET')
# # stock_comments('MIND')
# stock_comments('UWMC')
# # stock_comments('EOD')
# stock_comments('AAPL')
# stock_comments('RKT')
# # stock_comments('CAN')
# # stock_comments('PLAY')
# # stock_comments('PLAY')
# stock_comments('WKHS')
# stock_comments('NIO')
# stock_comments('EDIT')
# stock_comments('CLF')
# stock_comments('OUT')
# # stock_comments('AMD')
# stock_comments('AMD')
# # stock_comments('NOW')
# stock_comments('SPCE')
# stock_comments('SEE')

