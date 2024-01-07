import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from requests_html import HTMLSession
import matplotlib.pyplot as plt

import investpy
# Gets the stock object from investing.com
def get_stock(stock_symbol):
    stock=investpy.search_quotes(text=stock_symbol,products=['stocks'],countries=['india'],n_results=1)
    return stock
def fetch_recent_data(stock_symbol):
    stock=get_stock(stock_symbol)
    recent_data=stock.retrieve_recent_data()
    technical_indicators = stock.retrieve_technical_indicators(interval="daily")
    print(technical_indicators)
    # print(recent_data.plot.box())
    return recent_data
def fetch_historical_data(stock_symbol,from_date,to_date):
    stock=get_stock(stock_symbol)
    # from_date '01/01/2019'
    historical_data = stock.retrieve_historical_data(from_date=from_date, to_date=to_date)
    # print(historical_data.plot.box())
    return historical_data
def get_tech_indicators(stock_symbol,interval='daily'):
    # if (interval==''):
    #     interval='daily'
    stock=get_stock(stock_symbol)
    tech_indicators=stock.retrieve_technical_indicators(interval=interval)
    print(tech_indicators)  
    return tech_indicators   



## EXPERIMENTAL
# function attempting screener login
def screener_login():
    # with requests.Session() as session:
    with HTMLSession() as session:
        url='https://www.screener.in/login/'
        # Below Two lines will include user id and password for logi nto your screener
        
        USERNAME='Dummy USER ID' 
        PASSWORD='Dummy PASSWORD'
        session.get(url)
        csrftoken=session.cookies['csrftoken']
        login_data=dict(csrfmiddlewaretoken=csrftoken,username=USERNAME,password=PASSWORD,next='')
        session.post(url,data=login_data,headers={'origin':'https://www.screener.in',
            'Referer':'https://www.screener.in/login/?',
            'sec-fetch-mode':'same-origin',
        'sec-ch-ua':'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'})
        page=session.get('https://www.screener.in/dash/')
        return session

def get_roce(stock,session):
    # driver=webdriver.Chrome()
    url='http://www.screener.in/company/'+str(stock)+'/consolidated/'
    headers={'authority':'www.screener.in',
        'path':'/company/EICHERMOT/consolidated/',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'sec-fetch-mode':'navigate',
        'sec-fetch-site':'same-origin',
        'sec-fetch-user':'?1',
        'Referer':'https://www.screener.in/dash/'}
    # driver.get(url,headers=headers)
    # page=session.get(url,headers=headers,timeout=(100, 27))
    # s=HTMLSession()
    response=session.get(url)
    # r = urllib.request.urlopen(url)
    # soup=BeautifulSoup(page.content,'html.parser')
    soup=BeautifulSoup(response.html.render(),'html.parser')
    # driver.quit()
    # soup=BeautifulSoup(r.read(),'html.parser')

    # print(soup.contents)
    ratios=soup.select('.company-ratios li span')
    # print(ratios)
    for item in ratios:
        if item.string is not None:
            print(item.string)


