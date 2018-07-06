#
#
#
# printing a list recursively and iteratively
# searching for a number in a list
# sum of a list

def print_list_iterative(l):
    while len(l) >= 1:
        print(l[0])
        l = l[1:]

def print_list_recursive(l):
    if len(l) >= 1:
        print(l[0])
        print_list_recursive(l[1:])


def search_list_iterative(l, item):
    i = 0
    while i < len(l):
        if l[i] == item:
            return True
        i += 1
    return False

def search_list_recursive(l, item):
    if len(l) == 0:
        return False 
    elif l[0] == item: # if item is the first element, then return the index
        return True
    else:
        return search_list_recursive(l[1:], item)
    
def sum_list_iterative(l):
    i = 0
    total = 0
    while i < len(l):
        total += l[i]
        i += 1
    return total

def sum_list_recursive(l):
    if len(l) == 0:
        return 0
    else:
        return sum_list_recursive(l[1:]) + l[0]
















