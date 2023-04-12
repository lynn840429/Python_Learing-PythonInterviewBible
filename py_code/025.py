from functools import wraps
from time import time


def record_time(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("record_time")
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}执行时间: {time() - start}秒')
        return result
        
    return wrapper



@record_time
def add(a, b):
    return a+b

res = record_time(add(1, 6))
