# M1
items = [12, 5, 7, 10, 8, 19]
items = [x ** 2 for x in items if x % 2]
print(items)    # [25, 49, 361]

# M2
items = [12, 5, 7, 10, 8, 19]
print(list(filter(lambda x: x % 2, items)))
items = list(map(lambda x: x ** 2, filter(lambda x: x % 2, items)))
print(items)    # [25, 49, 361]

# M3
x = 10
fac = lambda x: __import__('functools').reduce(int.__mul__, range(1, x + 1), 1)
print(list(map(fac, range(x))))

gcd = lambda x, y: y % x and gcd(y % x, x) or x

# M4
x = 5
fact = lambda x: 1 if x == 0 else x * fact(x-1)
print(list(map(fact, range(x))))