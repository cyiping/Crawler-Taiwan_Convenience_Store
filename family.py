# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:42:02 2020

@author: User
"""

from  bs4 import BeautifulSoup
import requests


url1 = 'https://api.map.com.tw/net/familyShop.aspx?searchType=ShopList&type=&city=%E5%8F%B0%E5%8C%97%E5%B8%82&area=%E5%A4%A7%E5%AE%89%E5%8D%80&road=&fun=showStoreList&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC'

form1 = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,ja;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "api.map.com.tw",
        "Referer": "https://www.family.com.tw/Marketing/inquiry.aspx",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        }

req1 = requests.get(url1, headers = form1)
print(req1.text)

