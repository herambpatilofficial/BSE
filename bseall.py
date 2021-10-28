'''
This code returns information and advice of 
all BSE stocks in a single click!
The file of stock codes is given in this repository
as BSE.csv
'''
import numpy as np
from pandas import *
from bsedata.bse import BSE


bse = read_csv('BSE.csv', usecols=['Scrip Code'])

codelist = bse['Scrip Code'].tolist()

b = BSE()
 
for i in range(1,876):
  code = str(codelist[i])

  

  sv = float(b.getQuote(code)["currentValue"])
  wap = float(b.getQuote(code)["weightedAvgPrice"])
  compname = b.getQuote(code)["companyName"]
 
 
  if int(float(b.getQuote(code)["currentValue"])) > int(float(b.getQuote(code)["weightedAvgPrice"])):
    print(f"{i+1} {compname} Current Value: {sv} Average Value:{wap} : Sell")
      
      
    
  else:
      
    print(f"{i+1} {compname} Current Value: {sv} Average Value:{wap} : Buy")
 
