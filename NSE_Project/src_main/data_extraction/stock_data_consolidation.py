import stock_object 
import stock_price_extraction
import pandas as pd

# three_yrs_ago = datetime.now() - relativedelta(years=3)
#start_date = (datetime.now() - relativedelta(years=3)).strftime('%Y-%m-%d')
#print(start_date)
#(date.today()-timedelta(days=365*3)).strftime('%Y-%m-%d')
#end_date = (date.today()-timedelta(days=1)).strftime('%Y-%m-%d')

#df_nse = pd.read_csv('C:\\Users\\shiva.reddy\\Personal_Projects\\NSE_Project\\Input\\NSE_Listed_Companies_SectorWise.csv',sep='~')
df_nse = pd.read_csv('Input/NSE_Listed_Companies_SectorWise.csv',sep='~')

# Consolidation DataFrames declaration
df_final_stock_prices = pd.DataFrame()

df_nse_temp = df_nse.iloc[:3]

for index ,row in df_nse_temp.iterrows():
    print(row)
    print('Company : ',row['Ticker'])
    stock = stock_object.Stock(row['nse_ticker'])
    stock_obj = stock.getStockObject()

    stock_price_obj = stock_price_extraction.StockPriceExtraction(stock_obj , row['Ticker'])
    df_stock_price_company_wise = stock_price_obj.getPriceHistory()

        # All Listed companies- Day level Price information of the stock consolidation
    df_final_stock_prices = pd.concat([df_final_stock_prices,df_stock_price_company_wise],ignore_index=True)
    
    
print(len(df_final_stock_prices))
print(df_final_stock_prices.head())
