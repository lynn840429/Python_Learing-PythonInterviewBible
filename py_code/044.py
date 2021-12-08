prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

prices_sorted_1 = sorted(prices, key=lambda x: prices[x], reverse=True)
print(prices_sorted_1)

prices_sorted_2 = dict(sorted(prices.items(), key=lambda item: item[1], reverse=True))
print(prices_sorted_2)

prices_sorted_3 = sorted(prices.values(), reverse=True)
print(prices_sorted_3)

print(prices.keys())
print(prices.values())