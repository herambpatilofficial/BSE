#This code can be used to get full information about the stock
from bsedata.bse import BSE
#BSE refers to Bombay Stock Exchange
b = BSE()


code = input("Enter Stock Code: ")
name = (b.getQuote(code)["companyName"])
print(name)
if int(float(b.getQuote(code)["currentValue"])) > int(float(b.getQuote(code)["weightedAvgPrice"])):
  print("sell")
else:
  print("Buy")

print(b.getQuote(code))