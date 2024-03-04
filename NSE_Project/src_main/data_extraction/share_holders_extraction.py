from common_parameters import CommonParameters

class ShareHoldersExtraction(CommonParameters):

    def __init__(self,stock_object,company):
        super().__init__(stock_object,company)	

    def getMajorHolders(self):
        major_holders = self.stock_object.major_holders
        major_holders['ticker'] =  self.Company

        return major_holders

    def getInstitutionalHolders(self):
        institutional_holders = self.stock_object.institutional_holders
        institutional_holders['ticker'] =  self.Company

        return institutional_holders

    def getMutualFundHolders(self):
        mutualfund_holders = self.stock_object.mutualfund_holders
        mutualfund_holders['ticker'] =  self.Company

        return mutualfund_holders

    def getInsiderTransactions(self):
        insider_transactions = self.stock_object.insider_transactions
        insider_transactions['ticker'] =  self.Company

        return insider_transactions

    def getInsiderPurchases(self):
        insider_purchases = self.stock_object.insider_purchases
        insider_purchases['ticker'] =  self.Company

        return insider_purchases

    def getRosterHolders(self):
        insider_roster_holders = self.stock_object.insider_roster_holders
        insider_roster_holders['ticker'] =  self.Company

        return insider_roster_holders



