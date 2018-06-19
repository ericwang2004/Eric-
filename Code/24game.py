##
#
#

from itertools import permutations, product

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

def evaluate(numbers, operations):
    
    i = len(operations)-2
    
    ops = {'+':add, '-':subtract, '*':multiply, '/':divide}
    try:
        total = ops[operations[i+1]](numbers[i+1], numbers[i+2])
            
        while i >= 0:
            total = ops[operations[i]](numbers[i], total)
            i -= 1

    except ZeroDivisionError:
        pass
    else:
        return total

operators = ['+', '-', '*', '/']

def format_answer(numbers, operators):
    num_operators = len(operators)
    answer = ''
    for i in range(num_operators-1):
        answer += str(numbers[i]) + operators[i] + '('
    answer += str(numbers[-2]) + operators[-1] + str(numbers[-1]) + ')'*(num_operators - 1)
    return answer

def solve(numbers):
    for x in permutations(numbers):
        for y in product(operators, repeat=3):
            try:
                if abs(evaluate(x, y)-24) <= 10**-8:
                    print(format_answer(x, y))
            except TypeError:
                continue

solve([8, 8, 3, 3])
