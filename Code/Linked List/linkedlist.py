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

        
        # not sure how to do without if statement
        pointer = self.head
        for i in range(1, y):
            try:
                pointer = pointer.next_ # check if there exists a node after pointer
            except AttributeError:
                print('y out of bounds')
                return
        if y == 0:
            new_node = LinkedListNode(x, pointer)
            self.head = new_node
        else:
            new_node = LinkedListNode(x, pointer.next_)
            pointer.next_ = new_node

    """
	L: 5 --> 3 --> 9 --> -2 --> 100
    delete(9)
    L: 5 --> 3 --> -2 --> 100
    
    3.next_ = 3.next_.next_
    """
    # Delete the first occurrence of x
    def delete(self, x):
        pointer = self.head
        if not self.find(x):
            print("not found")
            return
        if pointer.value == x:
            self.head = pointer.next_
        else:
            while pointer.next_.value != x:
                pointer = pointer.next_
            pointer.next_ = pointer.next_.next_

    def __repr__(self):
        return self.head.__repr__()

# Convert a list to a LinkedList
"""
L = [5, 3, 9, -2, 100]
------------------------------

Make the head:

head = LinkedListNode(5, 1)
	where 5 is the value and 1 is some temporary value

------------------------------

2nd element:

node = LinkedListNode(3, 1)
head.next_ = node
head = LinkedListNode(5, LinkedListNode(3, 1))
head = node

head now points to LinkedListNode(3, 1)

------------------------------

3rd element (now i = 2)

node = LinkedListNode(9, 1)
head.next_ = node
head =  LinkedListNode(3, 1) ==>  LinkedListNode(3, node) = LinkedListNode(3, LinkedListNode(9, 1))


"""
def list_to_linked_list(L):
    head = LinkedListNode(L[0], 0)
    ll = LinkedList(head)
    for i in range(1, len(L)):

        node = LinkedListNode(L[i], 0)
        head.next_ = node
        head = node
    return ll

def iscyclic(ll):
    p1 = ll.head
    p2 = ll.head.next_
    while p2.next_ != 0 and p2.next_.next_ != 0 and p1.next_ != 0:
        if id(p1) == id(p2):
            return True
        p2 = p2.next_.next_
        p1 = p1.next_
    return False



array = [-25, 27, -4, 24, 12, 26, -74, -9, 67, -6, -31, -50, -28,
 40, 70, -69, 98, -89, -87, -40, 54, -64, -51, 56, 76, 81,
 99, 13, -18, -50, -70, 43, -69, -41, -21, 27, 91, 23, -94,
 17, 73, -8, 67, 40, 45, 52, 54, 95, -50, -10, -79, 65, 52,
 27, 69, 8, -40, 34, -76, -82, 2, -16, 58, 13, 27, 8, -84,
 3, -30, 21, 11, -10, -71, -89, 66, 22, -89, 24, 54, 92, -82,
 -71, -4, -36, -58, 22, -60, -51, -48, -35, -33, -6, -53, -37,
 -28, 55, -79, -44, 72, 35]

ll = list_to_linked_list(array)
pointer = ll.head
while pointer.next_ != 0:
    pointer = pointer.next_
pointer.next_ = ll.head.next_.next_ # 35.next_ = -4
print(iscyclic(ll)) # True







