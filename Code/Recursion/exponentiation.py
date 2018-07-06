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
        if d == 1:
            result = result**2 * a
        else: # d = 0
            result = result**2
    return result

def exp2_recursive(a, binary_b):
    #binary_b = bin(b)[2:]
    # assume binary_b is already in binary
    # this doesn't work
    if len(binary_b) == 0:
        return 1
    else:
        if binary_b[0] == '1':
            return exp2_recursive(a, binary_b[1:])**2*a
        else:
            return exp2_recursive(a, binary_b[1:])**2





