#
#
##

import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

fib_cache = {}
def fibonacci(n):
    if n == 1:
        fib_cache[1] = 1
        return 1
    elif n == 2:
        fib_cache[2] = 1
        return 1
    else:
        if n in fib_cache:
            return fib_cache[n]
        fib_cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib_cache[n]

def fibonacci2(n):
    f_1 = 1
    f_2 = 1
    for i in range(3, n+1): # if n is 1 or 2, return 1
        f_3 = f_1 # to keep the original value of f_1 before changing it
        f_1 = f_1 + f_2 # definition of sequence
        f_2 = f_3 # switched f_2 to original value of f_1
    return f_1

def collatz(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return collatz(n/2)+1
    else:
        return collatz(3*n+1)+1

def left_right(n, s):
    if len(s) == n:
        print(s)
    else:
        left_right(n, s+'r')
        left_right(n, s+'l')

n = 35

start = time.perf_counter()
print(fibonacci(n))
end = time.perf_counter()
print(end-start)


start = time.perf_counter()
print(fibonacci2(n))
end = time.perf_counter()
print(end-start)










