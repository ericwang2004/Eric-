# Circular queues
#
#
#

from stack import Stack

class Queue:

    def __init__(self):
        self.elements = []
        self.size = 0
        self.head = 0
        self.tail = -1

    def push(self, value):
        # appends new elements to the right side
        self.elements.append(value)
        self.size += 1
        self.tail += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Tried to pop from empty Queue") # pop from the left
        else:
            self.head += 1
            self.size -= 1
            return self.elements[self.head-1]

    def peek(self):
        return self.elements[self.head]

    def is_empty(self):
        return self.size == 0

    def __repr__(self):
        return str(self.elements[self.head:])

class CircularQueue:

    def __init__(self):
        self.elements = []
        self.limit = 10
        self.head = 0
        self.tail = -1

    def push(self, value):
        self.tail += 1
        if len(self.elements) >= self.limit:
            self.tail = 0
            self.elements[0] = value
        else:
            self.elements.append(value)
                          
    def pop(self):
        popped = self.elements[self.head]
        self.head += 1
        
        return popped

    def __repr__(self):
        return str(self.elements)
    
        
        

def reverse(q):
    r = Queue()
    s = Stack()
    size = q.size
    for i in range(size):
        s.push(q.pop())
    for i in range(size):
        r.push(s.pop())
    return r

q = CircularQueue()
for i in range(1, 11):
    q.push(i)

print(q) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
q.push(100)
print(q, q.head, q.tail)













