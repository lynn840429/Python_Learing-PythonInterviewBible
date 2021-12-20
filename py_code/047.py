def list_depth(items):
    if isinstance(items, list):
        '''
        isinstance(object, classinfo)
        - object: 实例对象。
        - classinfo: 可以是直接或间接类名、基本类型或者由它们组成的元组。
        '''
        max_depth = 1
        for item in items:
            print("item :", item, ", max_depth :", max_depth)
            max_depth = max(list_depth(item) + 1, max_depth)
        return max_depth
    return 0

items = [[1, [1, [2, 3]]], [2, [3]]]
print(list_depth(items))
print(isinstance.__doc__)