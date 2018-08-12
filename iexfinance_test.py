#IExFinance
#DNel

from iexfinance import Stock
from iexfinance import get_historical_data
from datetime import datetime, timedelta
from datetime import date
from iexfinance import get_stats_intraday
from iexfinance import get_available_symbols
import pandas as pd

#import datetime

# Set Date Variables
todays_date = str(date.today())
todays_timestamp = str(datetime.today())
yesterdays_date = str(date.today() - timedelta(days=1))
start = datetime(2013,1,1)
end = todays_date

# Get List of ticker symbols
full_ticker_info_dict = get_available_symbols(output_format='pandas')[:40]

ticker_symbol_list = [d['symbol'] for d in full_ticker_info_dict]

# ticker_name_list = [d['name'] for d in full_ticker_info_dict]
# ticker_date_list = [d['date'] for d in full_ticker_info_dict]
# ticker_isEnabled_list = [d['isEnabled'] for d in full_ticker_info_dict]
# ticker_type_list = [d['type'] for d in full_ticker_info_dict]
# ticker_id_list = [d['iexId'] for d in full_ticker_info_dict]

# blanks = [i for i,e in enumerate(ticker_name_list) if e==""]

columns = ('open','high','low','close','volume','ticker')

df_initial = pd.DataFrame(columns=columns)
#df_initial['index_col'] = df_initial.index 

counter = 0

for s in ticker_symbol_list:
	df = get_historical_data(s,start = start, end = end, output_format='pandas')
	df['ticker'] = s
	df_initial = df_initial.append(df)
	print(counter)
	print(s)
	counter +=1

print(df_initial)

path = "/Users/dnelson/Documents/csv_downloads/"

df_initial.to_csv(path+"historical_prices_"+yesterdays_date+".csv")
print("File Saved")


# qw = 0
# for n in range(400):
# 	print(qw)
# 	print(ticker_symbol_list[n])
# 	print(ticker_name_list[n])
# 	print(ticker_date_list[n])
# 	print(ticker_isEnabled_list[n])
# 	print(ticker_type_list[n])
# 	print(ticker_id_list[n])
# 	print("")
# 	print("")
# 	print("")

# 	qw =qw +1
# print(blanks)


#print(ticker_name_list)


# print(full_ticker_info_dict)
# Troubleshooting
# another_count = 0
# for symbol in ticker_symbol_list:
# 	print (another_count)
# 	print(symbol)
# 	another_count = another_count+1

#print(len(ticker_symbol_list))

# symbols = ('AMAL','ABEOW')

# print("Current Prices: ")
# for x in symbols:
# 	tsla = Stock(x)
# 	tsla.get_open()
# 	y = tsla.get_price()
# 	print(x, y)

# test_ticker = "AMAL"
# tsla = Stock(test_ticker)
# tsla.get_open()
# print(test_ticker)
# print(tsla.get_price())
# df = get_historical_data(test_ticker,start = start, end = end, output_format='pandas')
# df['ticker'] = test_ticker
# print(df)

# df.to_csv(test_ticker+"_"+yesterdays_date+".csv")

#	df.to_csv(s+"_"+yesterdays_date+".csv")



# df = get_historical_data(test_ticker,start = start, end = end, output_format='pandas')
# df.to_csv(test_ticker+"_"+yesterdays_date+".csv")









