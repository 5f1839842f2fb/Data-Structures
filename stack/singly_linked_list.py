
class Node:
    def __init__(self, value, nextnode = None):
        self.value = value
        self.nextnode = nextnode

    def backlink(self, previousnode):
        previousnode.nextnode = self


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        if self.head:
            self.tail.nextnode = Node(value)
            self.tail = self.tail.nextnode
        else:
            newnode = Node(value)
            self.head = newnode
            self.head.nextnode = newnode
            self.tail = newnode  # FFS, was trying self.head = Node(value) and self.tail = Node(value),
                                 # making two separate node instances

    def __str__(self):
        listy = []
        if self.head:
            currentnode = self.head
            while 1 != 0:
                listy.append(currentnode.value)
                if currentnode != self.tail:
                    currentnode = currentnode.nextnode
                else:
                    return str(listy)

    def remove_head(self):
        if not self.head:
            return None
        rv = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.nextnode
        return rv

    def remove_tail(self):
        pass

    def contains(self, value):
        if self.head:
            currentnode = self.head
            contained = False
            while not contained:
                if currentnode.value == value:
                    return True
                if currentnode == self.tail:
                    return False
                currentnode = currentnode.nextnode
        return False

    def get_max(self):
        max = None
        if self.head:
            max = self.head.value
            currentnode = self.head
            while 1 != 0:
                if currentnode.value > max:
                    max = currentnode.value
                if currentnode == self.tail:
                    return max
                currentnode = currentnode.nextnode
        return max


ll = LinkedList()
ll.add_to_tail(1)
print(ll)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)
print(ll)
print(ll.contains(3))