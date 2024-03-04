from common_parameters import CommonParameters

class BalanceSheetExtraction(CommonParameters):

    def __init__(self,stock_object,company):
        super().__init__(stock_object,company)

    def getBalanceSheetYearly(self):
        balance_sheet_yearly = self.stock_object.balance_sheet
        balance_sheet_yearly['ticker'] =  self.company

        return balance_sheet_yearly

    def getBalanceSheetQuarterly(self):
        balance_sheet_quarterly = self.stock_object.quarterly_balance_sheet
        balance_sheet_quarterly['ticker'] =  self.company

        return balance_sheet_quarterly


