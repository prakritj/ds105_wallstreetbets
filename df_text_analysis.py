import pickle
import nltk
import csv
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
import pandas as pd
from nltk.tokenize import word_tokenize
import numpy

df_comments=pd.read_pickle('WSB_Comments.pickle')
print(len(df_comments))

stop_words=set(stopwords.words("english"))
custom_stop_words =["!",":",".",",","'","..."]
stop_words.update(custom_stop_words)
print(type(stop_words))
ticker_df=pd.DataFrame()
i=0
for comment in df_comments.itertuples():
    i+=1
    body = comment.body
    words = word_tokenize(body)
    for word in words:
        for char in word:
            if not char.isalpha(): #William included check with custom_stop_words, need to check Data
                word.replace(char,"")
        if (len(word)==3) or (len(word)==4) and word.isupper():
            if (len(ticker_df) != 0):
                if word in ticker_df.ticker.values:
                    index = ticker_df.index[ticker_df.ticker == word][0]
                    ticker_df.at[index,'frequency']+=1
                    ticker_df.at[index,'score']+=comment.score
                else:
                    ticker_df = ticker_df.append({
                        'ticker':word,
                        'frequency':int(1),
                        'score':comment.score
                    }, ignore_index=True)
            else:
                ticker_df = ticker_df.append({
                    'ticker':word,
                    'frequency':int(1),
                    'score':comment.score
                }, ignore_index=True)
    if i % 1000 == 0:
        print('On Comment: ', i)

all_stocks_df = pd.read_csv('nasdaq_screener.csv', usecols=['Symbol'])
all_stocks_list = all_stocks_df['Symbol'].tolist()
clean_tickers_df = pd.DataFrame()

for dirty in ticker_df.itertuples():
    if dirty.ticker in all_stocks_list:
        clean_tickers_df = clean_tickers_df.append({
            'ticker':dirty.ticker,
            'frequency':dirty.frequency,
            'score':dirty.score
        }, ignore_index=True)
clean_tickers_df.sort_values(by='score', inplace=True,ascending=False)
clean_tickers_df.to_csv(r'clean_tickers.csv')