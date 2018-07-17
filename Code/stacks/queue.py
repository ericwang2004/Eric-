#
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
        self.limit = 100

    def push(self, value):
        # appends new elements to the right side
        self.elements.append(value)
        self.size += 1
        self.tail += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Tried to pop from empty Queue")
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

def reverse(q):
    r = Queue()
    s = Stack()
    size = q.size
    for i in range(size):
        s.push(q.pop())
    for i in range(size):
        r.push(s.pop())
    return r

q = Queue()
for i in range(1, 6):
    q.push(i)
r = reverse(q)
print(r)
















