#
#
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
    for char in eq:
        if char == '(':
            s.push(1)
        elif char == ')':
            try:
                s.pop()
            except Exception:
                return False
    return s.is_empty()







        
