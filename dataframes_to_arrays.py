import pandas as pd
import numpy as np
import pickle
import json

tickers = pickle.load(open('top_23_with_sectors.pickle', 'rb'))
tickers
tickers.reset_index(drop=True, inplace=True)

print(tickers.index)
print(tickers.columns)
tickers=tickers.drop(columns='row')
print(tickers)
ticker_array=tickers.to_numpy()
ticker_dict = tickers.to_dict()
print(ticker_array)
print(ticker_dict)
data = list(ticker_dict)
new_array = np.array(data)
print(new_array)
# test_array = tickers.as_matrix()
# print(test_array)

lol = tickers.values.tolist()
print(lol)
lol = map(str,lol)

ticker_array = map(str,ticker_array)
with open("output.txt", "w") as txt_file:
    for line in ticker_array:
        txt_file.write(" ".join(line) + "\n")



with open('data.json', 'w') as fp:
    json.dump(ticker_dict, fp)