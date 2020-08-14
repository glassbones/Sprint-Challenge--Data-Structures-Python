class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.root = None
        self.count = 0

    def append(self, item):
        # if capacity <= count ---------------------------------------------
        if self.capacity <= self.count:
            n = self.count - self.capacity
            current = self.root
            if n > 0:
                while n > 0:
                    current = current.next
                    n -= 1
            current.setData(item)
            self.count += 1
       # if list is empty     ---------------------------------------------
        elif self.root == None: 
            #set item as root
            self.root = Node(item)
            #set item.next to itself
            self.root.next = self.root
            self.count += 1
        else:
        # if multiple items in list ---------------------------------------------
        # set current to 2nd item in ring
            current = self.root.next
            # itterate until the next item in ring is the root
            while current.next != self.root:
                current = current.next
            
            # set last item in the ring before self.root to item
            current.next = Node(item)
            # connect it to the root
            current.next.next= self.root
            self.count += 1

    def get(self):
        arr = []
        current = self.root

        # itterate through ring
        while current.next != self.root:
            # append all values until last value
            arr.append(current.data)
            current = current.next

        # append last value
        arr.append(current.data)
        return arr