# comment

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

        if y == 0: # check if element is to be inserted at the beginning
            new_node = DoubleLinkedListNode(x, pointer, 0) # set new_node to point to the original head
            self.head = new_node # make new_node the new head
            new_node.next_.previous_ = new_node # make the second node point to the new_node
            
        else:
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
    
    def delete(self, x):
        pointer = self.head
        if pointer.value == x: # check if deleting first element
            pointer.next_.previous_ = 0 
            self.head = pointer.next_
            # set previous of second element to 0 and head of list to second element
            return

        while pointer.next_ != 0 and pointer.next_.value != x: #check if there exists a next element
            pointer = pointer.next_
        if pointer.next_ == 0: # verify that item is an element in the list
            print('not found')
            return
        
        pointer.next_ = pointer.next_.next_
        if pointer.next_ != 0:
            pointer.next_.previous_ = pointer



node1 = DoubleLinkedListNode(10, 0, 0)
node2 = DoubleLinkedListNode(5, 0, node1)
node3 = DoubleLinkedListNode(3, 0, node2)
node4 = DoubleLinkedListNode(1, 0, node3)
node1.next_ = node2
node2.next_ = node3
node3.next_ = node4

DLL = DoubleLinkedList(node1)
DLL.delete(5)
print(DLL)
