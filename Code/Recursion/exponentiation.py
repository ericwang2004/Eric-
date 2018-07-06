#
#
#
#

import time

def exp(a, b): # compute a**b
    c = a
    for i in range(1, b):
        a *= c
    return a

def exp2(a, b): # iteratively
    result = 1
    binary_b = bin(b)[2:]
    for d in binary_b:
        if d == '1':
            result = result**2 * a
        else: # d = 0
            result = result**2
    return result

def exp2_recursive(a, b):
    if b == 1:
        return a
    if b % 2 == 0:
        return exp2_recursive(a**2, b/2)
    else: # b % 2 == 1
        return exp2_recursive(a**2, (b-1)/2)*a

start = time.perf_counter()
exp(2, 1000000)
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
exp2(2, 1000000)
end = time.perf_counter()
print(end-start)



