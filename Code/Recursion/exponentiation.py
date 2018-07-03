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

def exp_recursive(a, b):
    pass # friday

def exp2(a, b): # iteratively
    pass

def exp2_recursive(a, b):
    pass






start = time.perf_counter()
print(exp(2, 10000))
end = time.perf_counter()
print(end-start)
