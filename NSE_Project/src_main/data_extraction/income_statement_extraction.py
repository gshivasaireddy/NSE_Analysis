from common_parameters import CommonParameters

class IncomeStatementExtraction(CommonParameters):

    def __init__(self,stock_object):
        super().__init__(stock_object)

    def getIncomeStatementYearly(self):
        income_statement_yearly = self.stock_object.income_stmt
        return income_statement_yearly

    def getIncomeStatementQuarterly(self):
        income_statement_quarterly = self.stock_object.quarterly_income_stmt
        return income_statement_quarterly