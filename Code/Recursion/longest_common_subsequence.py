# Tuesday: 
# 1.) time w/ perf_counter and O() in terms of length of string
# 2.) comment this code and other code
# 3.) skype

import time
import random
import string

def lcs(a, b):

    lcs.count += 1

    if a == "" or b == "": 
        return 0
    if a[0] == b[0]: 
        return lcs(a[1:], b[1:])+1
    else:
        return max(lcs(a[1:], b), lcs(a, b[1:])) 

already_computed = {}

def lcs_memoized(a, b):
    # same as above, but if any lcs() has already been computed,
    # then retrieve it from already_computed to avoid spending extra time
    # reduces from O(2**n) to O(
    #

    lcs_memoized.count += 1

    if (a, b) in already_computed:
        #print(a, b, 'already in dictionary')
        return already_computed[(a, b)]
    else:
        if a == "" or b == "":
            already_computed[(a, b)] = 0
            return already_computed[(a, b)]
        if a[0] == b[0]:
            already_computed[(a, b)] = lcs_memoized(a[1:], b[1:])+1
            return already_computed[(a, b)] 
        else:
            already_computed[(a, b)] = max(lcs_memoized(a[1:], b), lcs_memoized(a, b[1:]))
            return already_computed[(a, b)]

for l in range(2, 10):
    a = "".join(random.choice(string.ascii_lowercase) for x in range(l))
    b = "".join(random.choice(string.ascii_lowercase) for x in range(l))

    print(l, a, b)
    lcs.count = 0
    lcs_memoized.count = 0

    lcs(a, b)
    lcs_memoized(a, b)

    print(lcs.count, lcs_memoized.count)

