from itertools import islice

def fib(a = 0, b = 1):
    yield a
    while True:
        yield b
        a, b = b, a + b

a = list(islice(fib(), 20))
print(a)        