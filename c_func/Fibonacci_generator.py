def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        n = n + 1
        yield b 
        a, b = b, a+b