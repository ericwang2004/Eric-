# 1. Balanced parentheses
# 2. Evaluate postfix expression
#
#


class Stack:
    
    def __init__(self):
        self.elements = []
        self.size = 0

    def push(self, value):
        # appends new elements to the right side
        self.elements.append(value)
        self.size += 1

    def pop(self):
        # removes rightmost element
        if self.is_empty():
            raise Exception('tried to pop from empty stack')
        else:
            last = self.elements[-1]
            del self.elements[-1]
            self.size -= 1
            return last

    def peek(self):
        # returns rightmost element
        return self.elements[-1]

    def is_empty(self):
        return self.size == 0
    
    def __repr__(self):
        return str(self.elements)

def is_balanced(eq):
    s = Stack()
    parens = {')':'(', ']':'[', '}':'{', '>':'<'}
    for char in eq:
        if char in parens.values(): # the parens before the first right parens must be its corresponding left parens
            s.push(char)
        elif char in parens.keys():
            try:
                if parens[char] != s.pop(): # if the stack is empty when tried to pop, the parens are not balanced
                    return False
            except Exception:
                return False
    return s.is_empty() # check if the number of each left/right parens is matching

def eval_expr(n1, n2, op):
    # eval_expr(1, 2, +) -> 3
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == 'x':
        return n1 * n2
    else: # op == '/'
        return n1/n2

def eval_postfix(expr):
    # "1234+/-" -> (((4+3)/2)-1)
    s = Stack()
    for char in expr:
        if char in '0123456789': # if char is a number
            s.push(int(char))
        else: # if char is in [+, -, x, /]
            s.push(eval_expr(s.pop(), s.pop(), char))
    return s.pop() # the result is the only number in s

print(eval_postfix("12+34x/"))






        
