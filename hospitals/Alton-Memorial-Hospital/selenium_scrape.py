# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:39:53 2020
Name : Scrape chargemaster from javascript enable site
@author: TAZ
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

def scrape_data_js(pages=2**30):
    driver = webdriver.Firefox(log_path='/tmp/geckodriver.log')

    # Scrape data upto pages
    page_id = 1
    arr = []
    while page_id<pages:
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
    #Save original  
    try:
        df.to_csv('main.csv')   
    except Exception as e:
        print('Error Writing file: {}'.format(e))
    return df.to_html()


if __name__ == '__main__':
    print(scrape_data_js(1))