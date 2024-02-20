import yfinance as yf

class Stock:

    def __init__(self,company_ticker):
        self.company_ticker = company_ticker

    

    def getStockObject(self):
        stock_object = yf.Ticker(self.company_ticker)

        return stock_object

