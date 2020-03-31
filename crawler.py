# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:18:23 2020

@author: usem
"""
import requests
import bs4 as BeautifulSoup
import json

url1 = 'https://data.covid19info.live/processeddata.js'
a = requests.get(url1).json()
b = json.dumps(a)
f=open('data.txt','w')
f.write(b)
f.close()

print(a)
