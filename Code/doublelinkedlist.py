# For Tuesday:
#		1. Constructor for DoubleLinkedList
#		2. Write a __repr__ for both classes
#		3. Insertion in a DoubleLinkedList
#		4. For DoubleLinkedList, write a method to print the list backwards

class DoubleLinkedListNode:
    def __init__(self, value, next_, previous_):
        self.value = value
        self.next_ = next_
        self.previous_ = previous_

class DoubleLinkedList:
    # you know how to do this

    
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
        pass
      
