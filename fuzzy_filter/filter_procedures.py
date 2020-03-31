# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:56:02 2020
Name: Filter non procedural elements using Fuzzy String Matching
@author: TAZ
"""


from bs4 import BeautifulSoup
import requests

procedures_list = []
#Scrape all procedures and store it in list li
for c in "abcdefghijklmnopqrstuvwxyz":
    url = "https://www.medicinenet.com/procedures_and_tests/alpha_{}.htm".format(c)
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    procedures_list.extend([x.text for x in soup.select('#AZ_container li a')])
    
print(procedures_list)

#Export List as csv file
import pandas as pd
ser = pd.Series(procedures_list)
ser.to_csv('Available Procedures.csv',index=False)

from fuzzywuzzy import process

# Import chargemaster csv file as pandas DataFrame
df = pd.read_excel('../test/HCMC.xlsx')
# Take 'Item Description' Series of the DataFrame 
description_list = df['Item Description']

#Indivual Item accuracy check 
id = 138
print(description_list[id]) # DRAINAGE OF HEMATOMA COMPLEX
res = process.extract(description_list[id], procedures_list, limit=3)
print(res)
'''[('Abstinence Method of Birth Control (Natural Methods of Birth Control)', 86), 
 ('Arthroplasty (Joint Replacement Surgery Of The Hand)', 86),
 ('Balloon Angioplasty Of Heart (Coronary Angioplasty)', 86)]'''

# Check for procedure if in list
print( process.extract('endro', procedures_list, limit=3))

ans = []
for des in description_list[:100]:    
    score = process.extract(des, procedures_list, limit=1)[0]
    if 60 < score[1]:
        ans.append(des)
        print(des, score)
    
print(len(ans))
# 79