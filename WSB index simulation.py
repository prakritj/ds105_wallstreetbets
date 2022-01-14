import pickle
import csv
import pandas as pd
import yfinance as yf
import plotly.express as px
import os

top_10_tickers = []
all_tickers = pickle.load(open('filtered_clean_tickers.pickle', 'rb'))
all_tickers
all_tickers.reset_index(drop=True, inplace=True)
for i in range(0,9):
    ticker = str(all_tickers.loc[i,['ticker']][0])
    #print(all_tickers.loc[i,['ticker']])
    top_10_tickers.append(ticker)
print(top_10_tickers)

top_10_df = all_tickers
top_10_sectors = []
def get_stock_data(ticker):
    ticker = yf.Ticker(ticker)
    ticker_history = ticker.history(period="5mo")
    ticker_history = ticker_history.drop(['Open','High','Low','Volume','Dividends','Stock Splits'], axis = 1)
    return ticker_history
    # print(type(ticker_history))
    # fig = go.Figure()
    # fig.add_trace(go.Candlestick())
    # fig.add_trace(go.Candlestick(x=ticker_history.index, open=ticker_history['Open'], high = ticker_history['High'], low = ticker_history['Low'], close = ticker_history['Close'], name = 'market data'))
    # fig.update_layout(title=f'{i} share price', yaxis_title = 'Stock Price (USD)')
    # fig.write_image(f"/Users/williamsong/PycharmProjects/pythonProject/{i}.jpeg")
    # fig.to_image(format="jpeg", width = 2560, height = 1440, scale = 3, engine="kaleido")
    # print("industry: ", ticker_industry)
    # ticker_info_df = pd.DataFrame(ticker_info.items(),columns=['Characteristic','Value'])

GME_df = get_stock_data('GME')
AMC_df = get_stock_data('AMC')
PLTR_df = get_stock_data('PLTR')
NOK_df = get_stock_data('NOK')
SNDL_df = get_stock_data('SNDL')
WISH_df = get_stock_data('WISH')
TSLA_df = get_stock_data('TSLA')
CLOV_df = get_stock_data('CLOV')
MVIS_df = get_stock_data('MVIS')
CLNE_df = get_stock_data('CLNE')

stocks_average_dict = dict()
for ind in GME_df.index:
    GME_df.at[ind,'Close'] = (0.4055558807*100)/191.23 * float(GME_df['Close'][ind])
    AMC_df.at[ind, 'Close'] = (0.2320198619*100)/46.19 * float(AMC_df['Close'][ind])
    PLTR_df.at[ind,'Close'] = (0.1019778602*100)/23.29 * float(PLTR_df['Close'][ind])
    NOK_df.at[ind, 'Close'] = (0.05042339309*100)/5.47 * float(NOK_df['Close'][ind])
    SNDL_df.at[ind, 'Close'] = (0.04196115858*100)/0.89 * float(SNDL_df['Close'][ind])
    WISH_df.at[ind, 'Close'] = (0.03997812131*100)/11.14 * float(WISH_df['Close'][ind])
    TSLA_df.at[ind, 'Close'] = (0.03469077224*100)/656.95 * float(TSLA_df['Close'][ind])
    CLOV_df.at[ind, 'Close'] = (0.03236559914*100)/9.27 * float(CLOV_df['Close'][ind])
    MVIS_df.at[ind, 'Close'] = (0.0310443246*100)/15.93 * float(MVIS_df['Close'][ind])
    CLNE_df.at[ind, 'Close'] = (0.02998302826*100)/9.16 * float(CLNE_df['Close'][ind])


combined_df = pd.concat([GME_df, AMC_df, PLTR_df, NOK_df, SNDL_df, WISH_df, TSLA_df, CLOV_df, MVIS_df, CLNE_df], axis=1)
print(combined_df)
combined_df['Return (%)'] = combined_df.sum(axis=1) - 100
print(combined_df)
combined_df = combined_df.drop(columns = ['Close'])
print(combined_df)
fig = px.line(combined_df, x=combined_df.index, y="Return (%)", title="WSB Index Performance - ex post")
fig.show()

# fig = px.line(combined_df, x=combined_df.index, y="Index Value (USD)", title="WSB Index Performance - ex ante")
# # fig.write_image(f"/Users/williamsong/PycharmProjects/pythonProject/WSB_index_performance.jpeg")
# # fig.to_image(format="jpeg", width=2560, height=1440, scale=3, engine="kaleido")
# fig.show()
# top_23_df.insert(3,"Industry",top_23_sectors)
# top_23_df.to_pickle('top_23_with_sectors.pickle')
# top_23_df.to_csv(r'top_23_with_sectors.csv', mode = 'w')

# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(ticker_info_df)

# top_11 = all_tickers.head(13)
# print(top_11)
# for i in range(2,13):
#     print(top_11[i:i+1].ticker)