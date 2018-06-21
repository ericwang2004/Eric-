# Linked List

"""
A = [10, 5, 3, 1]

The base pointer of A is at memory address 100

Memory		Value
-----------------
100			10
101			5
102			3
103			1
...

A[0] --> get 100 + 0
A[2] --> get 100 + 2 = 102 -> 3


 Memory address:
     100		       500            202
+----+------+     +----+-----+     +----+-----+ 
| 10 | 500  | --> | 5  | 202 | --> | 3  | 
+----+------+     +----+-----+     +----+

The entire thing is a LinkedList
Each box in the list is called a LinkedListNode
    - Has two fields
        1. Value (10, 5, 3, 1, ...)
    	2. Pointer

"""

class LinkedListNode:
    # value is an integer
    # next_ is another LinkedListNode
    def __init__(self, value, next_):
        self.value = value
        self.next_ = next_

    # Finish this for Friday
    def __repr__(self):
        if self.next_ == 0:
            return str(self.value)
        return "{}, {}".format(self.value, self.next_)

	
  
class LinkedList:
  	# head is a LinkedListNode
    def __init__(self, head):
        self.head = head
  
    # Search if x is in the LinkedList
    # x is an integer
    def find(self, x):
        pointer = self.head
        while pointer.next_ != 0:
            if pointer.value == x:
                return True
            pointer = pointer.next_
        if pointer.value == x:
            return True
        return False

    # x is an integer
    # Insert a LinkedListNode with the value of x to the end of the LinkedList
    def append(self, x):
        new_node = LinkedListNode(x, 0)
        pointer = self.head
        while pointer.next_ != 0:
            pointer = pointer.next_
        pointer.next_ = new_node
        
    
    # x, y are integers
    # Insert a LinkedListNode with the value of x at position y of the LinkedList
    def insert(self, x, y):
        # [10, 5, 3, 1].insert(2, 1) = [10, 2, 5, 3, 1]
        pointer = self.head
        if y == 0:
            new_node = LinkedListNode(x, pointer)
            self.head = new_node
        else:
            for i in range(1, y):
                pointer = pointer.next_
            new_node = LinkedListNode(x, pointer.next_)
            pointer.next_ = new_node
            
        

      
node4 = LinkedListNode(1, 0)
node3 = LinkedListNode(3, node4)
node2 = LinkedListNode(5, node3)
node1 = LinkedListNode(10, node2)

LL = LinkedList(node1)
  
# Expect True
print(LL.find(10))

# Expect True
print(LL.find(1))

# Expect False
print(LL.find(100))

print(node1) # 10, 5, 3, 1
LL.append(15) 
print(node1) # 10, 5, 3, 1, 15
LL.insert(2, 0)
print(LL.head) # 2, 10, 5, 3, 1, 15
