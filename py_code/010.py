def multiply():
    return [lambda x: i * x for i in range(4)]
    #return (lambda x: i * x for i in range(4))

print([m(100) for m in multiply()])