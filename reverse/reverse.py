class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def set_head(self, new_head):
        self.head = new_head

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if (self.head == None or self.head.next == None):
            return self.head

        # current starts as the 2nd node in the list
        current = self.head.next
        # prev stars
        prev = self.head
        self.head.next = None

        while current.next != None:
            # ref next node
            target = current.next
            # set current.next to prev node
            current.set_next(prev)
            #move foward
            prev = current
            current = target

        # set last node as head and link it to the rest of the nodes
        self.set_head(current)
        self.head.set_next(prev)
        
        return self
        
