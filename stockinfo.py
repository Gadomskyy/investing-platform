import requests
import pprint


#using the alpha vantage stock info API
api_key = 'ETJJUR8UI8715QI8'

class stockInfo:
    def __init__(self, api_key):
        self.api_key = api_key
        #IBM set as default ticker
        self.ticker = "IBM"
        self.interval = '60min'
        self.update_url()

    def update_url(self):
        self.url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={self.ticker}&interval={self.interval}&apikey={self.api_key}'

    def getStockData(self, ticker):
        self.ticker = ticker
        self.update_url()
        r = requests.get(self.url)
        data = r.json()
        return data

    def getLatestStockPrice(self, ticker):
        selectedStock = self.getStockData(ticker)
        lastData = list(selectedStock[f'Time Series ({self.interval})'].items())[0][1]
        #"4. close" value is the latest known value
        lastValue = lastData['4. close']
        return lastValue
