#import stock_object
import yfinance as yf

class StockPriceExtraction:

    def __init__(self,stock_object,company):
        self.stock_object =  stock_object
        self.company = company

    def getPriceHistory(self):
        historical_price_data = self.stock_object.history(period="1d", start="2021-01-01").reset_index()
        historical_price_data['ticker'] = self.company

        return historical_price_data