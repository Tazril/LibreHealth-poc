# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:38:33 2020
Name: Simple Dictionary for Testing
@author: TAZ
"""

# Simple Dictionary

from bs4 import BeautifulSoup
import requests


word = input('Enter the word of which you want to find the meaning: ')

# Get the meaning by scrapping www.vocabulary.com
url = "https://www.vocabulary.com/dictionary/" + word
source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')
soup1 = soup.find(class_="short")

# If certain word's meaning is not found
try:
    soup1 = soup1.get_text()
    import re
    res = [ re.sub('\n|\t|\r','',x.text) for x in soup.select('#pageContent h3')]
    print ('Meanings')
    for x in res: print(x)
except AttributeError:
    print('Cannot find such word! Check spelling.')
input('Enter Key to Exit')

