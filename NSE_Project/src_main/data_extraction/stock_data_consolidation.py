import stock_object 
import stock_price_extraction as spe
import balance_sheet_extraction as ble 
import income_statement_extraction as ise
import share_holders_extraction as she
import cashflow_extraction as ce
import pandas as pd

# three_yrs_ago = datetime.now() - relativedelta(years=3)
#start_date = (datetime.now() - relativedelta(years=3)).strftime('%Y-%m-%d')
#print(start_date)
#(date.today()-timedelta(days=365*3)).strftime('%Y-%m-%d')
#end_date = (date.today()-timedelta(days=1)).strftime('%Y-%m-%d')

df_nse = pd.read_csv('C:\\Users\\shiva.reddy\\Personal_Projects\\NSE_Project\\Input\\NSE_Listed_Companies_SectorWise.csv',sep='~')

#df_nse = pd.read_csv('Input/NSE_Listed_Companies_SectorWise.csv',sep='~')

# Consolidation DataFrames declaration
df_final_stock_prices = pd.DataFrame()

df_nse_temp = df_nse.iloc[:2]

for index ,row in df_nse_temp.iterrows():
    print(row)
    print('Company : ',row['Ticker'])
    stock = stock_object.Stock(row['nse_ticker'])
    stock_obj = stock.getStockObject()

    # price history
    print('Price History: ')
    stock_price_obj = spe.StockPriceExtraction(stock_obj , row['Ticker'])
    df_stock_price_company_wise = stock_price_obj.getPriceHistory()

    # balance sheet
    balance_sheet_obj =  ble.BalanceSheetExtraction(stock_obj,row['Ticker'])
    df_balance_sheet_quartely = balance_sheet_obj.getBalanceSheetYearly()
    df_balance_sheet_yearly =  balance_sheet_obj.getBalanceSheetYearly()

    print('Balance sheet: ')
    print(df_balance_sheet_quartely)
    print(df_balance_sheet_yearly)

    # income statement
    income_stmt_obj  = ise.IncomeStatementExtraction(stock_obj,row['Ticker'])
    df_income_stmt_yearly = income_stmt_obj.getIncomeStatementYearly()
    df_income_stmt_quarterly = income_stmt_obj.getIncomeStatementQuarterly()

    print('Income Statement : ')
    print(df_income_stmt_yearly)
    print(df_income_stmt_quarterly)


    # cashflow
    cashflow_obj =  ce.CashFlowExtraction(stock_obj,row['Ticker'])
    df_cashflow_yearly =  cashflow_obj.getCashFlowYearly()
    df_cashflow_quarterly =  cashflow_obj.getCashFlowQuarterly()

    print('Cashflow : ')
    print(df_cashflow_yearly)
    print(df_cashflow_quarterly)


    # All Listed companies- Day level Price information of the stock consolidation
    df_final_stock_prices = pd.concat([df_final_stock_prices,df_stock_price_company_wise],ignore_index=True)
    
    
print(len(df_final_stock_prices))
print(df_final_stock_prices.head())
