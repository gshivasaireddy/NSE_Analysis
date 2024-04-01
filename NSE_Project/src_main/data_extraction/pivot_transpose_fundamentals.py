import pandas as pd

class PivotTranspose:

    @staticmethod
    def getTransposedConsolidated(dataframes,columns):
        transposed_consolidated_df  = pd.DataFrame()
        for i in range(len(columns)):
            specific_stock = dataframes[i].T.reset_index()
            specific_stock['ticker']=columns[i]
            transposed_consolidated_df = pd.concat([transposed_consolidated_df,specific_stock])
        
        ticker_column = transposed_consolidated_df.pop('ticker')
        transposed_consolidated_df.insert(1,'ticker',ticker_column)
        return transposed_consolidated_df