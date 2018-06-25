# For Tuesday:
# 1. Constructor for DoubleLinkedList
# 2. Write a __repr__ for both classes
# 3. Insertion in a DoubleLinkedList
# 4. For DoubleLinkedList, write a method to print the list backwards

class DoubleLinkedListNode:
    
    def __init__(self, value, next_, previous_):
        self.value = value
        self.next_ = next_
        self.previous_ = previous_

    def __repr__(self):
        if self.next_ == 0:
            return str(self.value)
        return '{} <--> {}'.format(str(self.value), self.next_)

class DoubleLinkedList:

    def __init__(self, head):
        self.head = head       
    
    
    # Insert value of x at position y
    """
    In a LinkedList, we will have
    
    1 --> 2 --> 3
    insert(4, 1)
    1 --> 4 --> 2 --> 3
    
    1 <--> 2 <--> 3
    insert(4, 1)
    1 <--> 4 <--> 2 <--> 3
    """
    def insert(self, x, y):
        # 10 - 5 - 3 - 1 .insert(2, 2) -> 10 - 5 - 2 - 3 - 1
        pointer = self.head
        # 10(*) - 5 - 3 - 1
        for i in range(1, y):
            pointer = pointer.next_ # pointer is at the yth node 10 - 5(*) - 3 - 1
        new_node = DoubleLinkedListNode(x, pointer.next_.next_, pointer) 
        pointer.next_ = new_node
        new_node.next_ = pointer.next_.next_.previous_
        new_node.next_.previous_ = new_node
        

    def __repr__(self):
        return self.head.__repr__()

    def print_backwards(self):
        pointer = self.head
        while pointer.next_ != 0:
            pointer = pointer.next_ # pointer is the last element
        while pointer.previous_ != 0:
            print(str(pointer.value)+', ', end='') # print on the same line
            pointer = pointer.previous_
        print(str(pointer.value)) # to print the first element at the end of the string
    
        



node1 = DoubleLinkedListNode(10, 0, 0)
node2 = DoubleLinkedListNode(5, 0, node1)
node3 = DoubleLinkedListNode(3, 0, node2)
node4 = DoubleLinkedListNode(1, 0, node3)
node1.next_ = node2
node2.next_ = node3
node3.next_ = node4

DLL = DoubleLinkedList(node1)
DLL.print_backwards() # 1, 3, 5, 10

DLL.insert(2, 2)
print(DLL.head)
DLL.print_backwards() # 1, 3, 2, 5, 10
