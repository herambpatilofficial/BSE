from bsedata.bse import BSE

b = BSE()


code = input("Enter Stock Code: ")
q = b.getQuote(code)
# gives information of getquote (refer readme.md)
q2 = b.getQuote(code)["companyName"]
# You can get any specific information from getQuote
# Refer readme.md

# Get Top Gainers
tg = b.topGainers()

# Get Top Losers
tL = b.topLosers()

# Get Period Trend
# This gives information of stock's trend in last some months.

periodTrend = b.getPeriodTrend(code, '3M')
# This function can get trends of 1, 3, 6 or 12 months

# Get Indices
indices = b.getIndices(category='corporate')
# Change Category if you want refer readme.md

allcodes = b.getScripCodes()
#Use this to get all listed companies and Scrip Codes











































