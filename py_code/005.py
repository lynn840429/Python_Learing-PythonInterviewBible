items = [12, 5, 7, 10, 8, 19]
items = list(map(lambda x: x ** 2, filter(lambda x: x % 2, items)))
print(items)    # [25, 49, 361]


items = [12, 5, 7, 10, 8, 19]   # [2, 0, 2, 0, 3, 4]
items2 = list(filter(lambda x: x%5, items))
print(items2)


items = [12, 5, 7, 10, 8, 19]
items = [x ** 2 for x in items if x % 2]
print(items)    # [25, 49, 361]