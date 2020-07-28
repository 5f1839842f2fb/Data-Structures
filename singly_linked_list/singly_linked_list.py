
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def backlink(self, previousnode):
        previousnode.next = self


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        if self.head:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        else:
            newnode = Node(value)
            self.head = newnode
            self.head.next = newnode
            self.tail = newnode

    def remove_head(self):
        if not self.head:
            return None
        rv = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return rv

    def remove_tail(self):
        if not self.head:
            return None
        rv = self.tail.value
        if self.head == self.tail:
            self.head = None
            return rv
        currentnode = self.head
        while currentnode.next is not self.tail:
            currentnode = currentnode.next
        self.tail = currentnode
        currentnode.next = None
        return rv

    def __str__(self):
        listy = []
        if self.head:
            currentnode = self.head
            while currentnode is not self.tail:
                listy.append(currentnode.value)
                currentnode = currentnode.next
            listy.append(currentnode.value)
        return str(listy)

    def __len__(self):
        length = 0
        if self.head:
            currentnode = self.head
            while currentnode is not self.tail:
                length += 1
                currentnode = currentnode.next
            length += 1
        return length

    def contains(self, value):
        if self.head:
            currentnode = self.head
            while currentnode is not self.tail:
                if currentnode.value == value:
                    return True
                currentnode = currentnode.next
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
                currentnode = currentnode.next
        return max

