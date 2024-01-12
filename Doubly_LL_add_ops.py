class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class createDoublyLL:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head is None:
            print("empty list")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.next

    def printLLReverse(self):
        print()
        if self.head is None:
            print("empty list")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.prev

    def insert_empty(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            print("LL not empty")

    def add_beg(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def add_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.next is not None:
                n = n.next

            n.next = newNode
            newNode.prev = n

    def add_after(self, data, x):
        if self.head is None:
            print("empty list")
        else:
            n = self.head

            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("element not present in the list")
            else:
                newNode = Node(data)
                newNode.next = n.next
                newNode.prev = n

                if n.next is not None:
                    n.next.prev = newNode
                n.next = newNode

    def add_before(self, data, x):
        if self.head is None:
            print("empty list")
        else:
            n = self.head

            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("element not present in the list")
            else:
                newNode = Node(data)
                newNode.next = n
                newNode.prev = n.prev
                if n.prev is not None:
                    n.prev.next = newNode
                else:
                    self.head = newNode
                n.prev = newNode


obj1 = createDoublyLL()
obj1.insert_empty(10)
obj1.add_beg(5)
obj1.add_after(10, 5)
obj1.add_end(15)
obj1.add_before(12,15)
obj1.printLL()
obj1.printLLReverse()
