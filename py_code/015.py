from functools import lru_cache


@lru_cache()
def change_money(total, c1=2, c2=3, c3=5):
    if total == 0:
        return 1
    if total < 0:
        return 0
    return change_money(total - c1) + change_money(total - c2) + change_money(total - c3)


#print(change_money(10))
print(change_money(6, 2, 3, 5))