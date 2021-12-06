class A(): 
    __val = 0
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value

    @value.deleter
    def value(self):
        del self.__value



obj = A(1)
print(obj.value)

obj.__value2 = 2
print(obj.__value2)

obj.value = 3
print(obj.value)

print(dir(A))
del obj.value