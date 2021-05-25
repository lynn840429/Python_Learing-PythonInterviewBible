
## M1
def dedup(items):
    no_dup_items = []
    seen = set()
    for item in items:
        if item not in seen:
            no_dup_items.append(item)
            seen.add(item)
    return no_dup_items

print(dedup([9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 8, 5]))

## M2
def dedup2(items):
    no_dup_items = []

    for item in items:
        if item not in no_dup_items:
            no_dup_items.append(item)
    
    return no_dup_items

print(dedup2([9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 8, 5]))

## M3
def dedup3(items):
    no_dup_items = set()

    for item in items:
        if item not in no_dup_items:
            no_dup_items.add(item)
    
    return no_dup_items

print(dedup3([9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 8, 5]))

## M4
def dedup4(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

print(dedup4([9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 8, 5]))

## M5
def dedup5(items):
    return sorted(set(items), key=items.index)

print(dedup5([9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 8, 5]))

## M6
def dedup6(items):
    no_dup_items = []
    return [no_dup_items.append(i) for i in items if not i in no_dup_items]

print(dedup5([9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 8, 5]))

