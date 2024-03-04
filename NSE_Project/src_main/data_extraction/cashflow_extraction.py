from common_parameters import CommonParameters

class CashFlowExtraction(CommonParameters):

    def __init__(self,stock_object,company):
        super().__init__(stock_object,company)

    def getCashFlowYearly(self):
        cash_flow_yearly = self.stock_object.cashflow
        cash_flow_yearly['ticker'] =  self.company

        return cash_flow_yearly

    def getCashFlowQuarterly(self):
        cash_flow_quarterly = self.stock_object.quarterly_cashflow
        cash_flow_quarterly['ticker'] =  self.company  # common step : can make it better to reduce redundancy

        return cash_flow_quarterly