from functools import wraps

def singleton(cls):
    """单例类装饰器"""
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


#@singleton
class President:
    def __init__(self, i=1):
        self.i = i
        print(i)

    def P_print(self):
        print("Class President: ", self.i)


P1 = President(1)
P1.P_print()
P2 = President(2)
P2.P_print()
