# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:13:44 2020

@author: User
"""

from  bs4 import BeautifulSoup
import requests

url1 = 'https://emap.pcsc.com.tw/EMapSDK.aspx'
form1 = {
        "commandid": "SearchStore",
        "city": "台北市",
        "town": "大安區",
        "roadname": "",
        "ID": "",
        "StoreName": "",
        "SpecialStore_Kind": "",
        "leftMenuChecked": "",
        "address": "",
       
        }

req1 = requests.post(url1, data = form1)
soup1 = BeautifulSoup(req1.content, 'xml')
data1 = soup1.findAll("GeoPosition")

for row in data1:
    print('PIOID: ' + row.find('POIID').text)
    print('店名: ' + row.find('POIName').text)
    print('座標(E): ' + row.find('X').text)
    print('座標(N): ' + row.find('Y').text)
    print('電話: ' + row.find('Telno').text)
    print('地址: ' + row.find('Address').text)
