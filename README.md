# BSE
Repository to access information of stocks in Bombay Stock Exchange.


### The code in this repository uses BSE API and conclusions made using the code in this repository are purely based on some properties of stock and are not professional advice.

## bse.py 
This code can be used to get full information about the stock

## bseadvice.py
This code returns stock name from 
stock code and returns advice 
whether to buy or sell depending on 
the weighted average price of stock.

## bseall.py
This code returns information and advice of 
all BSE stocks in a single click!
The file of stock codes is given in this repository
as BSE.csv

# How to use?
In your terminal,

first run 
`pip install bsedata`

Now run,
`pip install numpy`

Now run 
`pip install pandas`

## Information Accessible through GetQuote:

   2WeekAvgQuantity': '0.14 Lakh',
  '52weekHigh': '3298.00',
  '52weekLow': '1874.00',
  'buy': {'1': {'price': '0.00', 'quantity': '-'},
          '2': {'price': '0.00', 'quantity': '-'},
          '3': {'price': '0.00', 'quantity': '-'},
          '4': {'price': '0.00', 'quantity': '-'},
          '5': {'price': '0.00', 'quantity': '-'}},
  'change': '76.75',
  'companyName': 'V-MART RETAIL LTD.',
  'currentValue': '2255.80',
  'dayHigh': '2270.00',
  'dayLow': '2185.10',
  'faceValue': '10.00',
  'group': 'A  / S&P BSE 500',
  'industry': 'Department Stores',
  'lowerPriceBand': '1804.65',
  'marketCapFreeFloat': '1,883.72 Cr.',
  'marketCapFull': '4,095.05 Cr.',
  'pChange': '3.52',
  'previousClose': '2179.05',
  'previousOpen': '2199.65',
  'priceBand': '20%',
  'scripCode': '534976',
  'securityID': 'VMART',
  'sell': {'1': {'price': '0.00', 'quantity': '-'},
           '2': {'price': '0.00', 'quantity': '-'},
           '3': {'price': '0.00', 'quantity': '-'},
           '4': {'price': '0.00', 'quantity': '-'},
           '5': {'price': '0.00', 'quantity': '-'}},
  'totalTradedQuantity': '0.01 Lakh',
  'totalTradedValue': '0.13 Cr.',
  'updatedOn': '14 Jun 19 | 04:00 PM',
  'upperPriceBand': '2706.95',
  'weightedAvgPrice': '2239.58'

### Using the phrases in ' ' with getQuote gives that specific information about the stock.


## Top Gainers
{'LTP': '2,255.80',
   'change': '76.75',
   'pChange': '3.52',
   'scripCode': '534976',
   'securityID': 'VMART'},
  {'LTP': '274.30',
   'change': '9.25',
   'pChange': '3.49',
   'scripCode': '538835',
   'securityID': 'INTELLECT'}

### Top Gainers return the information in ''

## Top Losers
{'LTP': '82.05',
   'change': '-9.90',
   'pChange': '-10.77',
   'scripCode': '532617',
   'securityID': 'JETAIRWAYS'},
  {'LTP': '76.55',
   'change': '-7.85',
   'pChange': '-9.30',
   'scripCode': '500111',
   'securityID': 'RELCAPITAL'}

### Top Losers return the information in ''


## Period Trend data
Get Stock information for Specific period of time.
The available period options are '1M', '3M', '6M' and '12M'.

## Getting Indices
category parameter can be one of the following:



market_cap/broad

sector_and_industry

thematics

strategy

sustainability

volatility

composite

government

corporate

money_market

## Verify Scrip Code
`b.verifyScripCode('534976')`
Verify whether scrip code or BSE Stock code is valid or not



### You can use code in templates.py to make your own code and for that take help of readme.md

For any suggestions, mail on herambpatil2004@gmail.com
