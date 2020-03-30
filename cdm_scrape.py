#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:47:36 2020
Name: Scrape 115 hospitals' name and url
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

url = 'https://qz.com/1518545/price-lists-for-the-115-biggest-us-hospitals-new-transparency-law/'

source =  requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

data = []

for hospital in soup.find_all('td'):
    name = hospital.text
    url = hospital.a['href']
    
    print(name)
    print(url)
    print()
    
    data.append([name,url])

df = pd.DataFrame(data,columns=['name','url'])
df.to_csv('hospital_cdm.csv')

if not os.path.exists('hospitals'):
    os.mkdir('hospitals')

for name, url in  df.values:
    name = name.replace('.','').strip()
    if not os.path.exists('hospitals/'+name):
        os.mkdir('hospitals/'+name)
    with open('hospitals/'+name+'/link.txt','w') as f:   
        f.write('url='+url)

