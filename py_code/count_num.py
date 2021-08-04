from collections import Counter

def count_letters_1(items):
    result = {}
    for item in items:
        if isinstance(item, (int, float)):
            result[item] = result.get(item, 0) + 1
    return result

def count_letters_2(items):
    result = {}
    items.sort()
    for item in items:
        if item in result.keys():
            result[item] += 1
        else:
            result[item] = 1
    return result


a = [1, 1, 2, 3, 4, 7, 8, 8, 9, 5, 4, 2, 3, 6]
print(count_letters_1(a))
print(count_letters_2(a))
print(Counter(a))