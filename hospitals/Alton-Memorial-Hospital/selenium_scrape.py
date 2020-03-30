# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:39:53 2020
Name : Scrape chargemaster from javascript enable site
@author: TAZ
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time


driver = webdriver.Firefox()

page_id = 1
arr = []
while True:
    try:    # browse all pages till end
        driver.get("https://search.hospitalpriceindex.com/hospital/Alton-Memorial-Hospital/5358?page={}".format(page_id))
    except:
        break
    page_id+=1
    time.sleep(3)
    data = driver.page_source
    time.sleep(5)
    
    soup = BeautifulSoup(data,'lxml')
    # store data as 1D list
    elist =  [ x.text for x in soup.find_all('td') ]
    # reshaping
    for i in range(0,len(elist),3):
        arr.append(elist[i:i+3])



driver.close()   
import pandas as pd

df = pd.DataFrame(arr,columns=['code','description','charge'])
df.to_csv('main.csv')    
