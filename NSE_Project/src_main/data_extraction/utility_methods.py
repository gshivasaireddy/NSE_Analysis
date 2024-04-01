import pandas as pd

class Utility:

    @staticmethod
    def getTransposedMatrix(dataframe):
        return dataframe.T.reset_index()

    @staticmethod
    def setTickerField(dataframe,ticker):
        dataframe['ticker']=ticker
        return dataframe

    @staticmethod
    def consolidate(dataframes_list:list):
        consolidated_dataframe = pd.concat(dataframes_list)
        ticker_column = consolidated_dataframe.pop('ticker')
        consolidated_dataframe.insert(1,'ticker',ticker_column)
        return consolidated_dataframe

        

    # def getTransposedConsolidated(dataframes,columns):
    #     # transposed_consolidated_df  = pd.DataFrame()
    #     # for i in range(len(columns)):
    #     #     specific_stock = dataframes[i].T.reset_index()
    #     #     specific_stock['ticker']=columns[i]
    #     #     transposed_consolidated_df = pd.concat([transposed_consolidated_df,specific_stock])
        
    #     # ticker_column = transposed_consolidated_df.pop('ticker')
    #     # transposed_consolidated_df.insert(1,'ticker',ticker_column)

    #     return transposed_consolidated_df