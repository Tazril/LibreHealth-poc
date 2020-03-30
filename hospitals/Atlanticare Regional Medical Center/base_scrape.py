#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:46:45 2020
Name : Direct Scrape -> Download csv file directly
@author: taz
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

with open('link.txt') as f:
    csv_url = f.readline().split('=')[-1]

csv_file = requests.get(csv_url)

with open('main.csv','w') as f:
    f.write(csv_file.text)

df = pd.read_csv('main.csv')

df = df.rename(columns={'DESCRIPTION':'description','CHARGE':'charge'})

df.to_csv('charges.csv')


# Query any procedure 
def query(procedure):
    df = pd.read_csv('charges.csv',index_col=0)
    df = df.dropna()
    results = []
    for element in df.values:
        if procedure in element[0].lower():
            results.append({'name':element[0],'charge':element[1]})
    return results
    
'''
query('dialysis')
Out[36]: 
[{'charge': '5,190', 'name': 'CATH DIALYSIS PALINDROME(COVIDIEN'},
 {'charge': '1,332', 'name': 'CATH HEMODIALYSIS 13FR 5605240'},
 {'charge': '3,693', 'name': 'HEMODIALYSIS IP (W/1 MD EVAL)'},
 {'charge': '3,693', 'name': 'HEMODIALYSIS,LTACH,BEDSIDE'},
 {'charge': '3,217', 'name': 'HEMODIALYSIS-OUTPATIENT'},
 {'charge': '357', 'name': 'SET, HEMO CATH DIALYSIS'}]
 
'''
