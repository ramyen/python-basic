import yfinance as yf
import requests_cache

session = requests_cache.CachedSession('yfinance.cache')
session.headers['User-agent'] = 'my-program/1.0'
tesla = yf.Ticker("TSLA", session)

history = tesla.history(period= "1mo", interval="1d")
print(history)