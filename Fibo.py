# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fibr(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibr(n-1) + fibr(n-2)