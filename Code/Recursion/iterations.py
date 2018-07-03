#
#
#
#


# return n!
# O(n)
def factorial(n):
    product = 1
    if n == 0:
        return product
    while n != 0:
        product *= n
        n -= 1
    return product


# return the nth fibonacci number
# O(n)
def fibonacci(n):
    f_1 = 1
    f_2 = 1
    for i in range(3, n+1): # if n is 1 or 2, return 1
        f_3 = f_1 # to keep the original value of f_1 before changing it
        f_1 = f_1 + f_2 # definition of sequence
        f_2 = f_3 # switched f_2 to original value of f_1
    return f_1
        
# Collatz
# If n is even, n/2
# If n is odd, 3n+1
def collatz(n):
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n+1
    return count


def dec_to_binary(n): # needed for left_right function
    binary = ''
    while n != 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

# print all strings that consists of only l and r characters of length n
#
    
def left_right(n):
    for i in range(2**n): # each l corresponds to 1 and r corresponds to 0
        string = ''
        binary = dec_to_binary(i) # convert base 10 integer to binary
        length = 0 # in case the binary representation has less than n digits, the first few should be r's
        for c in binary: # parse string and replace ls with ls and 0s with rs
            length += 1
            if c == '1':
                string = string + 'l'
            else: # c = '0'
                string = string + 'r'
        string = 'r'*(n-length) + string # fill the first few places with r's
        print(string)
        


