from singly_linked_list.singly_linked_list import LinkedList

"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList(LinkedList):
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if not self.head:
            newnode = ListNode(value)
            self.head = newnode
            self.tail = newnode
        else:
            newnode = ListNode(value)
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None
        else:
            rv = self.head.value
            if self.head.next:
                self.head = self.head.next
                if self.head.next:
                    self.head.next.prev = self.head
            else:
                self.head = None
                self.tail = None
            return rv
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if not self.head:
            newnode = ListNode(value)
            self.head = newnode
            self.tail = newnode
        else:
            newnode = ListNode(value)
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.head:
            return None
        else:
            rv = self.tail.value
            if self.tail.prev:
                self.tail = self.tail.prev
                if self.tail.prev:
                    self.tail.prev.next = self.tail
            else:
                self.head = None
                self.tail = None
            return rv
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head == self.tail:
            pass
        else:
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
            if node == self.tail:
                self.remove_from_tail()
            self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head == self.tail:
            pass
        else:
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
            if node == self.head:
                self.remove_from_head()
            self.add_to_tail(node.value)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """


"""
ll = LinkedList()
ll.add_to_tail(100)
ll.add_to_tail(101)
ll.add_to_tail(105)
print(ll, ll.head.value, ll.tail.value)
print("removed value: " + str(ll.remove_head()))
print(ll, ll.head.value, ll.tail.value)
"""