from common_parameters import CommonParameters

class IncomeStatementExtraction(CommonParameters):

    def __init__(self,stock_object,company):
        super().__init__(stock_object,company)

    def getIncomeStatementYearly(self):
        income_statement_yearly = self.stock_object.income_stmt
        income_statement_yearly['ticker'] =  self.company

        return income_statement_yearly

    def getIncomeStatementQuarterly(self):
        income_statement_quarterly = self.stock_object.quarterly_income_stmt
        income_statement_quarterly['ticker'] =  self.company  # common step : can make it better to reduce redundancy

        return income_statement_quarterly