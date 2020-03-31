#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:46:45 2020
Name : Direct Scrape -> Download csv file directly
@author: taz
"""

import pandas as pd

def scrape_data():
    
    csv_url = 'https://www.atlanticare.org/assets/images/services/price-transparency/2019finalpricetransparencyforjan1.csv'
  
    # Convert to Dataframe    
    df = pd.read_csv(csv_url)
    # Save original
    try:
        df.to_csv('main.csv')
    except Exception as e:
        print('Error Writing file: {}'.format(e))
    # Rename columns
    df = df.rename(columns={'DESCRIPTION':'description','CHARGE':'charge'})
    # Save standard
    try:
        df.to_csv('charges.csv')
    except Exception as e:
        print('Error Writing file: {}'.format(e))
    # return html response    
    return df.to_html()


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
