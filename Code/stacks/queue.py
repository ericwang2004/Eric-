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
        
        self.limit = 10
        self.elements = [0]*self.limit
        self.size = 0
        self.head = 0
        self.tail = -1

    def push(self, value):
        if self.size >= self.limit:
            print('Cannot add more elements')
            return
        
        self.size += 1
        self.tail += 1
        self.tail %= self.limit
        self.elements[self.tail] = value
                          
    def pop(self):
        if self.size < 1:
            print('Cannot pop')
            return
        
        self.size -= 1
        popped = self.elements[self.head]
        self.head += 1
        self.head %= self.limit
        
        return popped

    def clear(self):
        while self.size > 0:
            self.pop()

    def __repr__(self):
        if self.size == 0:
            return str([])
        if self.head <= self.tail:
            return str(self.elements[self.head:self.tail+1])
        elif self.head > self.tail:
            return str(self.elements[self.head:]+self.elements[:self.tail+1])
        
        

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
for i in range(1, 6):
    q.push(i)
    print(q, q.head, q.tail) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
q.pop()
print(q, q.head, q.tail)

q.pop()
print(q, q.head, q.tail)

for i in range(6, 11):
    q.push(i)
    print(q, q.head, q.tail)

q.push(11)
print(q, q.head, q.tail)

q.push(12)
print(q, q.head, q.tail)

for i in range(1, 9):
    q.pop()
    print(q, q.head, q.tail)

q.clear()
print(q, q.head, q.tail)













