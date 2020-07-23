
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
        if not self.head:
            return None
        rv = self.tail.value
        if self.head == self.tail:
            self.head = None
            return rv
        currentnode = self.head
        while currentnode.nextnode is not self.tail:
            currentnode = currentnode.nextnode
        self.tail = currentnode
        currentnode.nextnode = None
        return rv

    def __str__(self):
        listy = []
        if self.head:
            currentnode = self.head
            while currentnode is not self.tail:
                listy.append(currentnode.value)
                currentnode = currentnode.nextnode
            listy.append(currentnode.value)
        return str(listy)

    def __len__(self):
        length = 0
        if self.head:
            currentnode = self.head
            while currentnode is not self.tail:
                length += 1
                currentnode = currentnode.nextnode
            length += 1
        return length

    def contains(self, value):
        if self.head:
            currentnode = self.head
            while currentnode is not self.tail:
                if currentnode.value == value:
                    return True
                currentnode = currentnode.nextnode
            if currentnode.value == value:
                return True
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
ll.add_to_tail(5)
print(ll)
print("length: " + str(len(ll)))
print(ll.contains(3))

ll.remove_tail()
print(ll)
print(ll.head.value)
print(ll.tail.value)
ll.remove_head()
print(ll)
print(ll.head.value)
print(ll.tail.value)
ll.remove_tail()
ll.remove_tail()
print(ll.head.value)
print(ll.tail.value)
ll.remove_tail()

print(ll)