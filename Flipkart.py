# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:52:33 2018

@author: Milan
"""
"""
Web Scrapper for scrapping Flipkart.
"""

import re
import requests
from bs4 import BeautifulSoup

url=input("Enter the URL you want to scrap : ")

Req=requests.get(url)
soup=BeautifulSoup(Req.text, 'html.parser')

ChoiceOrg='._2yAnYN'
DataList0=list()
for i in soup.select(ChoiceOrg):
    item=re.findall(r'^[A-Z].*',i.text)
    DataList0.append(i.text)
a=DataList0[0]
print('This flipkart page is about : %s' %(a))
#print(len(DataList0))

print("===============================================================================")



ChoiceOrg='._2cLu-l'
DataList=list()                 #ItemName
for i in soup.select(ChoiceOrg):
    item=re.findall(r'^[A-Z].*',i.text)
    DataList.append(i.text)
print(DataList)
print(len(DataList))
print("===============================================================================")

ChoiceOrg='._1vC4OE'
DataList1=list()                #Discountprice
for i in soup.select(ChoiceOrg):
    DataList1.append(i.text)
print(DataList1)
print(len(DataList1))
print("===============================================================================")

ChoiceOrg='._3auQ3N'
DataList2=list()                #Originalprice
for i in soup.select(ChoiceOrg):
    DataList2.append(i.text)
print(DataList2)
print(len(DataList2))
print("===============================================================================")

ChoiceOrg='.VGWI6T'
DataList3=list()                #Discount
for i in soup.select(ChoiceOrg):
    DataList3.append(i.text)
print(DataList3)
print(len(DataList3))
print("===============================================================================")

'''ChoiceOrg='._38sUEc'
DataList4=list()                #Review
for i in soup.select(ChoiceOrg):
    DataList4.append(i.text)
print(DataList4)
print(len(DataList4))
'''

#<h1 class="_2yAnYN">Sports Shoes</h1> heading 1 'Topic'
#<h1 class="_2yAnYN">T Shirts</h1>
#<a class="_2cLu-l" title="Billion PerfectFit Solid Men Round Neck Multicolor T-Shirt" 
#<div class="_1vC4OE">₹854</div>
#<div class="_3auQ3N">₹1,999</div>
#<div class="VGWI6T"><span>57% off</span></div>
#<span class="_38sUEc"><span><span>60,970 Ratings&nbsp;</span><span class="_1VpSqZ">&amp;</span><span>&nbsp;11,351 Reviews</span></span></span>

#<div class="_1vC4OE _1DTbR5">₹2,364</div>