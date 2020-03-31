# -*- coding: utf-8 -*-
"""

* Parse Data Table
https://covid19info.live/zh/

* BeautifulSoup parse table
https://leemeng.tw/beautifulsoup-cheat-sheet.html



"""
import requests
from bs4 import BeautifulSoup
import json

url1 = 'https://data.covid19info.live/processeddata.js'

'''
a = requests.get(url1).json()
b = json.dumps(a)
f=open('data.txt','w')
f.write(b)
f.close()

'''



url2 = "https://data.covid19info.live"
html2 = requests.get(url2)
sp2 = BeautifulSoup(html2.text, "html.parser")
st = sp2.find("table", {"class", })
print(st)