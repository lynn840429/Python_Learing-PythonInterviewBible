import copy

def cp(a=[]):
    a1_shellow_copy = a[:]
    a1_deep_copy = a

    a2_shellow_copy = copy.copy(a)
    a2_deep_copy = copy.deepcopy(a)

    print("Init a=", a, id(a))
    a[0] = 7
    a[3][1] = 4

    print("After a=", a, id(a))

    print("a[:]=", a1_shellow_copy, id(a1_shellow_copy))

    print("a=", a1_deep_copy, id(a1_deep_copy))

    print("copy.copy(a)=", a2_shellow_copy, id(a2_shellow_copy))
    
    print("copy.deepcopy(a)=", a2_deep_copy, id(a2_deep_copy))


a = [1, 2, 3, [4, 5, 6]]
cp(a)