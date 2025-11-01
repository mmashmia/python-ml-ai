def SquareIt(x):
    return x * x

print(SquareIt(2))

def DoSomething(f, x):
    return f(x)

print(DoSomething(SquareIt, 3))

print(DoSomething(lambda x: x * x * x, 3))
