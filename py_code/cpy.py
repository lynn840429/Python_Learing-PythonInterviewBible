'''
CPython: 把频繁使用的整数对象用一个叫small_ints的对象池缓存起来造成的。
small_ints缓存的整数值被设定为[-5, 256]这个区间，也就是说，
在任何引用这些整数的地方，都不需要重新创建int对象，
而是直接引用缓存池中的对象。如果整数不在该范围内，
那么即便两个整数的值相同，它们也是不同的对象。
'''
a, b, c, d = 1, 1, 1000, 1000
print(a is b, c is d)

def foo():
    e = 1000
    f = 1000
    print(e is f, e is d)
    g = 1
    print(g is a)

foo()