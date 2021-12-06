"""
def extend_list(val=0, items=[]):
    items.append(val)
    return items

list1 = extend_list(10)
print(list1)
list2 = extend_list(123, [])
list3 = extend_list('a')
list4 = extend_list(456, [])
list5 = extend_list(20)
list6 = extend_list()
list7 = extend_list(items=[789])
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
"""

fish = 6
while True:
    total, enough = fish, True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5