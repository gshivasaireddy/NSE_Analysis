import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os
import time
from datetime import date
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

os.listdir('nse_listed_companies_sector_wise')  # 'India_PLC_Sector_Industry_2023_MARCH.csv'

# stock price data
company_list = ['LTIM','GLOBAL','VERANDA','AGRITECH','RITES']

# Consolidation DataFrames declaration
df_final_stock_prices_consolidated = pd.DataFrame()

df_final_income_stmt_consolidated_yearly = pd.DataFrame()
df_final_balance_sheet_consolidated_yearly = pd.DataFrame()
df_final_cashflow_consolidated_yearly = pd.DataFrame()

df_final_income_stmt_consolidated_quarterly = pd.DataFrame()
df_final_balance_sheet_consolidated_quarterly = pd.DataFrame()
df_final_cashflow_consolidated_quarterly = pd.DataFrame()

for company in company_list:
    ticker_symbol =  f'{company}.NS'
    print(ticker_symbol)
    
    stock_object = yf.Ticker(ticker_symbol)
    
    # price info
    historical_price_data = stock_object.history(period="1d", start="2021-01-01", end=end_date).reset_index()
    historical_price_data['ticker'] = company
    
    # # show financials:
    # - income statement
    df_company_yearly_income_stmt = stock_object.income_stmt
    df_company_yearly_income_stmt['ticker'] = company
    df_company_quarterly_income_stmt = stock_object.quarterly_income_stmt
    df_company_quarterly_income_stmt['ticker'] = company
    
    # - balance sheet
    df_company_yearly_balance_sheet = stock_object.balance_sheet
    df_company_yearly_balance_sheet['ticker'] = company
    df_company_quarterly_balance_sheet =stock_object.quarterly_balance_sheet
    df_company_quarterly_balance_sheet['ticker'] = company
    
    # - cash flow statement
    df_company_yearly_cashflow =stock_object.cashflow
    df_company_yearly_cashflow['ticker'] = company
    df_company_quarterly_cashflow = stock_object.quarterly_cashflow
    df_company_quarterly_cashflow['ticker'] = company
    
    
    # All Listed companies- Day level Price information of the stock consolidation
    df_final_stock_prices = pd.concat([df_final_stock_prices,historical_price_data],ignore_index=True)
    
    # All companies yearly fundamentals consolidation(income statements , balance sheets , cashflows)
    df_final_income_stmt_consolidated_yearly = pd.concat([df_final_income_stmt_consolidated_yearly,df_company_yearly_income_stmt])
    df_final_balance_sheet_consolidated_yearly = pd.concat([df_final_balance_sheet_consolidated_yearly,df_company_yearly_balance_sheet])
    df_final_cashflow_consolidated_yearly= pd.concat([df_final_cashflow_consolidated_yearly,df_company_yearly_cashflow])
    
    # All companies quartely fundamentals consolidation(income statements , balance sheets , cashflows)
    df_final_income_stmt_consolidated_quarterly=pd.concat([df_final_income_stmt_consolidated_quarterly,df_company_quarterly_income_stmt])
    df_final_balance_sheet_consolidated_quarterly=pd.concat([df_final_balance_sheet_consolidated_quarterly,df_company_quarterly_balance_sheet])
    df_final_cashflow_consolidated_quarterly=pd.concat([df_final_cashflow_consolidated_quarterly,df_company_quarterly_cashflow])
    
    time.sleep(3)
    

df_final_stock_prices.head()



# Transposing income-statements , cashflows and balance sheets and finally consolidating
for company in company_list:
    ticker_symbol =  f'{company}.NS'
    print(ticker_symbol)
    
    stock_object = yf.Ticker(ticker_symbol)
    
    # # show financials:
    # - income statement
    df_company_yearly_income_stmt = stock_object.income_stmt
    df_company_yearly_income_stmt=df_company_yearly_income_stmt.T.reset_index()
    df_company_yearly_income_stmt['ticker'] = company
    df_final_income_stmt_consolidated_yearly = pd.concat([df_final_income_stmt_consolidated_yearly,df_company_yearly_income_stmt])
#     df_company_quarterly_income_stmt = stock_object.quarterly_income_stmt
#     df_company_quarterly_income_stmt['ticker'] = company

print(len(df_final_income_stmt_consolidated_yearly))
ticker_column = df_final_income_stmt_consolidated_yearly.pop('ticker')
df_final_income_stmt_consolidated_yearly.insert(1,'ticker',ticker_column)
df_final_income_stmt_consolidated_yearly.head()