# 1. Finish insertion_sort
# 2. comments
# 3. time both and O()

import time
import random

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

def merge(l1, l2):
    result = []
    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    for x in range(i, len(l1)):
        result.append(x)
    for y in range(j, len(l2)):
        result.append(y)

    return result


print(merge([1, 3, 4, 7], [2, 4, 6, 9]))





'''
test_list = [random.randrange(1, 101) for x in range(1, 101)]

start = time.perf_counter()
insertion_sort(test_list)
end = time.perf_counter()
print(end-start)
'''
