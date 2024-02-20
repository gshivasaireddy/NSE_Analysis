import pandas as pd


file_name = 'C:\\Users\\shiva.reddy\\Personal_Projects\\NSE_Project\\Input\\India_PLC_Sector_Industry_2023_MARCH.csv'


df_nse_stock = pd.read_csv(file_name)
df_nse_stock = df_nse_stock[df_nse_stock.Exchange=='NSE']
df_nse_stock['nse_ticker'] = df_nse_stock['Ticker']+'.NS'



print(len(df_nse_stock))
print(df_nse_stock.head())

df_nse_stock.to_csv('Input/NSE_Listed_Companies_SectorWise.csv',index=False,sep='~')


