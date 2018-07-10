# 1. Finish insertion_sort
# 2. comments
# 3. time both and O()



def selection_sort(l):
    
    for i in range(len(l)):
        j = l.index(min(l[i:]))
        l[i], l[j] = l[j], l[i]
        # print(l)
    return l

def insertion_sort(l):
    # [6, 5, 4, 3, 2, 1] -> [5, 6, 4, 3, 2, 1] -> [5, 4, 6, 3, 2, 1] -> [4, 5, 6, 3, 2, 1] ...
    # [4, 5, 6, 5.5] -> [4, 5, 5.5, 6]
    pass


l = [6, 5, 4, 3, 2, 1]
print(selection_sort(l))
