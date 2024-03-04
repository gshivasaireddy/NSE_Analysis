#import stock_object
from common_parameters import CommonParameters
import yfinance as yf

# Historical Stock Data at Day level
class StockPriceExtraction(CommonParameters):

    def __init__(self,stock_object,company):
        super().__init__(stock_object,company)

    def getPriceHistory(self):
        historical_price_data = self.stock_object.history(period="1d", start="2021-01-01").reset_index()
        historical_price_data['ticker'] = self.company

        return historical_price_data


