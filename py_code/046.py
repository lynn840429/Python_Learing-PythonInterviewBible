def more_than_half(items):
    temp, times = None, 0
    for item in items:
        if times == 0:
            temp = item
            times += 1
        else:
            if item == temp:
                times += 1
            else:
                times -= 1
    return temp


def more_than_half_2(items):
    items.sort()
    temp = -1
    targ_times = len(items)//2
    cout_times = 1

    for item in items:
        if (item==temp):
            cout_times += 1
        else:
            temp = item
            cout_times = 1
        
        if (cout_times>=targ_times):
            return temp

    return -1


def more_than_half_3(items):
    items.sort()
    temp = -1
    targ_times = len(items)//2

    for item in items:
        if (item==temp):
            targ_times -= 1
        else:
            temp = item
            targ_times = len(items)//2
        
        if (targ_times<=1):
            return temp

    return -1

    
#items = [1, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]
items = [1, 2, 3, 3, 3, 3, 3, 4, 5, 6]
print(more_than_half(items))
print(more_than_half_2(items))
print(more_than_half_3(items))