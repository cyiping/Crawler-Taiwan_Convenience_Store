# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:42:02 2020

@author: User
"""
import requests
from  bs4 import BeautifulSoup
import json

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

url1= 'https://www.family.com.tw/Marketing/inquiry.aspx'
html1 = requests.get(url1, headers = form1)
sp = BeautifulSoup(html1.text, "html.parser")

'''
# 這一段沒有預期的效果, 抓不到21縣市名稱

st = sp.find("showAdminArea1")

# 只好直接print(sp) , 直接抓到21縣市名稱, 直接丟到List

'''
showAdminArea1 = ["宜蘭縣","花蓮縣","台東縣","基隆市","台北市","新北市","桃園市","新竹市","新竹縣","苗栗縣","雲林縣","嘉義市","嘉義縣","台南市","高雄市","屏東縣","澎湖縣","金門縣","台中市","彰化縣","南投縣"]

'''
# storeTownList

    "post": "946",
    "town": "恆春鎮",
    "city": "屏東縣"

'''
with open ("test.txt", mode = "w") as file:
    for i in showAdminArea1:
        url1 = 'https://api.map.com.tw/net/familyShop.aspx?searchType=ShowTownList&type=&city='+ i + '&fun=storeTownList&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC'
        req1 = requests.get(url1, headers = form1)
        print(req1.text)
        a = json.dumps(req1.text).strip("storeTownList")
        file.write(a)
file.close()    
    
'''
url2= 'https://api.map.com.tw/net/familyShop.aspx?searchType=ShowTownList&type=&city=%E5%8F%B0%E5%8C%97%E5%B8%82&fun=storeTownList&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC'
req2 = requests.get(url2, headers = form1)
print(req2.text)


url3 = 'https://api.map.com.tw/net/familyShop.aspx?searchType=ShopList&type=&city=%E5%8F%B0%E5%8C%97%E5%B8%82&area=%E5%A4%A7%E5%AE%89%E5%8D%80&road=&fun=showStoreList&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC'


req3 = requests.get(url3, headers = form1)
print(req3.text)
'''