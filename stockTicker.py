#Jacob Barnes
tickersDict = dict({
    'GOOG': 1.11,
    'AAPL': 2.45,
    'AMZ': 3.98,
    'MSFT': 4.12,
    'VZ': 5.11,
    'KO': 6.12,
    'FB': 7.13,
    'F': 8.14,
    'T': 9.15,
    'COST': 10.16
})

ticker = input("Enter a ticker: ").upper()

#search for ticker, print results with f-string
if ticker in tickersDict:
    print(f"The value of {ticker} is currently ${tickersDict[ticker]:.2f}.")
else:
    print(f"Ticker {ticker} not found.")