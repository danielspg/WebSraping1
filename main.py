

"""
AUTHOR: SAURABH GAJBHIYE
ID: 2020PCS2028
Branch: MTech Information Security, IIT,Jammu.


THIS script will crawl the NSE.com and store the values of following stock
RELIANCE , SBIN, ASIANPAINT, TATAMOTORS, CIPLA

We will be storing the current price of these stocks in
the "STOCK_result.csv" file.

the script will run for 30 minutes.
and the updated value of stocks is recorded every 2 seconds.

"""



import requests
from bs4 import BeautifulSoup
import time

filename = "STOCK_result.csv"
f = open(filename, 'w')
headers = "RELIANCE , SBIN, ASIANPAINT, TATAMOTORS,CIPLA \n"

f.write(headers)


def fetch_NSE_stock_price(stock_code):
    stock_url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=' + str(
        stock_code)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(stock_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")
    for item in data_array:
        if 'lastPrice' in item:
            index = data_array.index(item) + 1
            latestPrice = data_array[index].split('"')[1]
            return float(latestPrice.replace(',', ''))





stock_code1 = "RELIANCE"
stock_code2 = "SBIN"
stock_code3 = "ASIANPAINT"
stock_code4 = "TATAMOTORS"
stock_code5 = "CIPLA"




t_iteration = 1000 #number of iterations
d_sleep = 2 #the price of stock is recorded every 2 seconds



iteration = 0
while iteration < t_iteration:
    current_stock_price1 = fetch_NSE_stock_price(stock_code1)
    current_stock_price2 = fetch_NSE_stock_price(stock_code2)
    current_stock_price3 = fetch_NSE_stock_price(stock_code3)
    current_stock_price4 = fetch_NSE_stock_price(stock_code4)
    current_stock_price5 = fetch_NSE_stock_price(stock_code5)
    print("{} , {} , {}, {}, {} ".format(current_stock_price1, current_stock_price2, current_stock_price3, current_stock_price3, current_stock_price4, current_stock_price5))
    print(str(current_stock_price1) + ',' + str(current_stock_price2) + ',' + str(current_stock_price3) + ',' + str(current_stock_price4)+ ',' + str(current_stock_price5), file=f)
    time.sleep(d_sleep)
    iteration = iteration + 1

f.close()

# End
