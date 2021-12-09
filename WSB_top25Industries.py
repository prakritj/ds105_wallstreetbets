import pickle
import csv
import pandas as pd
import yfinance as yf

top_tickers = []
all_tickers = pickle.load(open('filtered_clean_tickers.pickle', 'rb'))
all_tickers.reset_index(drop=True, inplace=True)
for stock in all_tickers.itertuples():
    ticker = stock.ticker
    #print(all_tickers.loc[i,['ticker']])
    top_tickers.append(ticker)
print(top_tickers)

top_sectors = []
for i in top_tickers:
    ticker = yf.Ticker(i)
    ticker_info = ticker.info
    # print(type(ticker_info))
    # print(ticker_info)
    ticker_sector = ticker_info['sector']
    # ticker_industry = ticker_info['industry']
    print(i)
    print("sector: ", ticker_sector)
    top_sectors.append(ticker_sector)
    # print("industry: ", ticker_industry)
    # ticker_info_df = pd.DataFrame(ticker_info.items(),columns=['Characteristic','Value'])
    # print(ticker_info_df)

all_tickers.insert(3,"Industry",top_sectors)
all_tickers.to_pickle('top_25_with_sectors.pickle')
all_tickers.to_csv(r'top_25_with_sectors.csv', mode = 'w')

# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(ticker_info_df)

# top_11 = all_tickers.head(13)
# print(top_11)
# for i in range(2,13):
#     print(top_11[i:i+1].ticker)