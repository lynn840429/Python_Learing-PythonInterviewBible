import random
import cProfile

a = 5
b = 30
x = [1, 3, 5, 7, 9]
seq = x

def random_test():
    print(random.random())
    print(random.uniform(a, b))
    print(random.randint(a, b))
    random.shuffle(x)
    print(x)
    print(random.choice(seq))

cProfile.run('random_test()')