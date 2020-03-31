# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:38:33 2020
Name: Simple Dictionary for Testing
@author: TAZ
"""

# Simple Dictionary

import requests


def scrape_csv(request):
    url = "https://raw.githubusercontent.com/Tazril/LibreHealth-poc/master/hospitals/Atlanticare%20Regional%20Medical%20Center/base_scrape.py"
    source = requests.get(url).text
    exec(source, globals())
    return scrape_data()

def scrape_js(request):
    url = "https://raw.githubusercontent.com/Tazril/LibreHealth-poc/master/hospitals/Alton-Memorial-Hospital/selenium_scrape.py"
    source = requests.get(url).text
    exec(source, globals())
    return scrape_data_js(2)

