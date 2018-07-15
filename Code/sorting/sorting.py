# 1. Insertion_sort iteratively
# 2. Comments
# 3. 

import time
import random
import sys

sys.setrecursionlimit(100000000)

def selection_sort(l):
    
    for i in range(len(l)):                 # loop through the list
        j = l.index(min(l[i:]))             # and each time swap the minimum element from the elements not considered yet
        l[i], l[j] = l[j], l[i]             # with the first element not considered (not necessarily the first element overall)
        # print(l)
    return l

def is_sorted(l):
    for i in range(len(l)-1):               # go through every element in the list
        if l[i] > l[i+1]:                   # if there exists an element > next element,
            return False                    # then the list is not sorted
    return True                             # if there does not exist an element > next element,
                                            # then the list is sorted
def insertion_sort(l):
    # [6, 5, 4, 3, 2, 1] -> [5, 6, 4, 3, 2, 1] -> [5, 4, 6, 3, 2, 1] -> [4, 5, 6, 3, 2, 1] ...
    # [4, 5, 6, 5.5] -> [4, 5, 5.5, 6]
    if is_sorted(l):                        # check if list is already sorted
        return l                            # if so, return the list
    
    else:                                   # if the list is not sorted
        i = 0
        while True:                         # go through the list until:
            if l[i] > l[i+1]:               # you find an element that is greater than the next element,
                l[i], l[i+1] = l[i+1], l[i] # in which case their positions are swapped,
                break                       # and proceed to run insertion_sort on the resulting modified list
            i += 1 
        return insertion_sort(l)

def insertion_iterative(l):
    for i in range(1, len(l)): # for each element in l
        j = i
        # print(l)
        while j > 0:
            if l[j] < l[j-1]: # continue switching the selected element until it is correctly placed
                l[j], l[j-1] = l[j-1], l[j]
                j -= 1
            else:
                break
    return l

def merge(l1, l2):
    
    result = []
    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:          # compare the elements of each list
            result.append(l1[i])    # if l1[i] is larger, increment i
            i += 1
        else:
            result.append(l2[j])    # if l2[j] is larger, increment j
            j += 1

    for x in range(i, len(l1)):     # one list will have no elements left to be sorted
        result.append(l1[x])        # and dump the elements of the other list into result
    for y in range(j, len(l2)):
        result.append(l2[y])

    return result

def mergesort(l):
    right = l[len(l)//2:] # partition l into two roughly equally sized list
    left = l[:len(l)//2]
    if len(l) == 1:
        return l
    else:
        return merge(mergesort(right), mergesort(left)) # sort each half and merge them

l = [6, 5, 3, 2, 3]
print(insertion_iterative(l))

