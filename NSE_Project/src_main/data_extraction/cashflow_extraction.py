from common_parameters import CommonParameters

class CashFlowExtraction(CommonParameters):

    def __init__(self,stock_object):
        super().__init__(stock_object)

    def getCashFlowYearly(self):
        cash_flow_yearly = self.stock_object.cashflow
        return cash_flow_yearly

    def getCashFlowQuarterly(self):
        cash_flow_quarterly = self.stock_object.quarterly_cashflow
        return cash_flow_quarterly