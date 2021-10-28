# This code returns stock name from 
# stock code and returns advice 
# whether to buy or sell depending on 
# the weighted average price of stock.
from bsedata.bse import BSE

b = BSE()


code = input("Enter Stock Code: ")
name = (b.getQuote(code)["companyName"])
print(name)
if int(float(b.getQuote(code)["currentValue"])) > int(float(b.getQuote(code)["weightedAvgPrice"])):
  print("sell")
else:
  print("Buy")
