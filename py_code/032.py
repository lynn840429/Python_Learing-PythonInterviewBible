class A:
    def who(self):
        print('A', end='')

class B(A):
    def who(self):
        super().who()
        print('B', end='')

class C(A):
    def who(self):
        super().who()
        print('C', end='')

class D(B, C):
    def who(self):
        super().who()
        print('D', end='')

item = D()
item.who()
print(D.__mro__)

#---------------------------------
class X(object):
    pass

class Y(object):
    pass

class Z(object):
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(A, B, Z):
    pass

# python2.3以后的版本里，MRO都是通过 C3 linearization 的方法计算
print(M.mro())
