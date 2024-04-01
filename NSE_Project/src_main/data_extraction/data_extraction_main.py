import stock_object 
import stock_price_extraction as spe
import balance_sheet_extraction as ble 
import income_statement_extraction as ise
import share_holders_extraction as she
import cashflow_extraction as ce
import warnings
import pandas as pd
from data_consolidation import DataConsolidation as dc
from pivot_transpose_fundamentals import PivotTranspose
warnings.filterwarnings('ignore')

nse_company_file = 'C:\\Users\\shiva.reddy\\Personal_Projects\\NSE_Analysis\\NSE_Analysis\\NSE_Project\Input\\NSE_Listed_Companies_SectorWise_Sample.csv'
df_nse = pd.read_csv(nse_company_file,sep='~')
df_nse =  df_nse.head(3)
df_nse.head()


# stores the output dataframes of each companies for later consolidation
income_statement_yearly_dfs = []
income_statement_quarterly_dfs = []

balance_sheet_yearly_dfs = []
balance_sheet_quarterly_dfs = []

cashflow_yearly_dfs = []
cashflow_quartely_dfs = []

price_history_dfs = []

for index,row in df_nse.iterrows():
    print('Company : ',row['Ticker'])
    stock = stock_object.Stock(row['nse_ticker'])
    stock_obj = stock.getStockObject()
    
    # price history 
    stock_price_obj = spe.StockPriceExtraction(stock_obj , row['Ticker'])
    df_stock_price_company_wise = stock_price_obj.getPriceHistory()
    price_history_dfs.append(df_stock_price_company_wise)
    
    # income statement yearly
    balance_sheet_obj =  ble.BalanceSheetExtraction(stock_obj,row['Ticker'])
    df_balance_sheet_quartely = balance_sheet_obj.getBalanceSheetQuarterly()
    df_balance_sheet_yearly =  balance_sheet_obj.getBalanceSheetYearly()
    balance_sheet_yearly_dfs.append(df_balance_sheet_yearly)
    balance_sheet_quarterly_dfs.append(df_balance_sheet_quartely)
    
df_stock_prices_consolidated = dc.consolidate(price_history_dfs)
df_balance_sheets_yearly_consolidated = PivotTranspose.getTransposedConsolidated(balance_sheet_yearly_dfs,columns=['LTIM','KPITTECH','HDFC'])
