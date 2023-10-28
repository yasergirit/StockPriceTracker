import yfinance as yf

data = yf.download(tickers= "ACX", period='1m', interval='1wk')

print("SBUX")