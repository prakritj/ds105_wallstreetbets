import pickle
import csv
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import os

top_23_tickers = []
all_tickers = pickle.load(open('filtered_clean_tickers.pickle', 'rb'))
all_tickers
all_tickers.reset_index(drop=True, inplace=True)
for i in range(0,23):
    ticker = str(all_tickers.loc[i,['ticker']][0])
    #print(all_tickers.loc[i,['ticker']])
    top_23_tickers.append(ticker)
print(top_23_tickers)

top_23_df = all_tickers
top_23_sectors = []
for i in top_23_tickers:
    ticker = yf.Ticker(i)
    ticker_info = ticker.info
    # print(type(ticker_info))
    # print(ticker_info)
    ticker_sector = ticker_info['sector']
    # ticker_industry = ticker_info['industry']
    print(i)
    print("sector: ", ticker_sector)
    ticker_history = ticker.history(period="YTD")
    print(ticker_history)
    print(ticker_history.index)
    for col in ticker_history.columns:
        print(col)
    # print(type(ticker_history))

    fig = go.Figure()
    fig.add_trace(go.Candlestick())
    fig.add_trace(go.Candlestick(x=ticker_history.index, open=ticker_history['Open'], high = ticker_history['High'], low = ticker_history['Low'], close = ticker_history['Close'], name = 'market data'))
    fig.update_layout(title=f'{i} share price', yaxis_title = 'Stock Price (USD)')
    fig.write_image(f"/Users/williamsong/PycharmProjects/pythonProject/{i}.jpeg")
    fig.to_image(format="jpeg", width = 2560, height = 1440, scale = 3, engine="kaleido")


    top_23_sectors.append(ticker_sector)
    # print("industry: ", ticker_industry)
    # ticker_info_df = pd.DataFrame(ticker_info.items(),columns=['Characteristic','Value'])
    # print(ticker_info_df)

top_23_df.insert(3,"Industry",top_23_sectors)
top_23_df.to_pickle('top_23_with_sectors.pickle')
top_23_df.to_csv(r'top_23_with_sectors.csv', mode = 'w')

# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(ticker_info_df)

# top_11 = all_tickers.head(13)
# print(top_11)
# for i in range(2,13):
#     print(top_11[i:i+1].ticker)