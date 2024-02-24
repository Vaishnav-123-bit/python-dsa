

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        print()
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

    def delete_beg(self):
        if self.head is None:
            print("empty LL")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("empty LL")
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.prev.next = None

    def del_byVal(self, x):
        if self.head is None:
            print("empty LL")
        elif self.head.next is None:
            if x == self.head.data:
                self.head = None
            else:
                print("Not included in LL ")
        else:
            if self.head.data == x:
                self.head = self.head.next
                self.head.prev = None
            else:
                n = self.head
                while n.next is not None:
                    if x == n.data:
                        break
                    n = n.next
                if n.next is not None:
                    n.next.prev = n.prev
                    n.prev.next = n.next
                else:
                    if n.data == x:
                        n.prev.next = None
                    else:
                        print("element not found")


obj1 = DoublyLinkedList()
while True:
    print("\nEnter choice:")
    print("1. Add_beg")
    print("2. Add_end")
    print("3. Add_after")
    print("4. Add_before")
    print("5. Delete_beg")
    print("6. Delete_end")
    print("7. Delete by value")
    print("8. PrintLL")
    print("9. Print revLL")
    print("10. Exit")

    choice=int(input("enter"))



    if choice == 1:
        data = int(input("Enter data: "))
        obj1.add_beg(data)
    elif choice == 2:
        data = int(input("Enter data: "))
        obj1.add_end(data)
    elif choice == 3:
        data = int(input("Enter data: "))
        x = int(input("Add after: "))
        obj1.add_after(data, x)
    elif choice == 4:
        data = int(input("Enter data: "))
        x = int(input("Add before: "))
        obj1.add_before(data, x)
    elif choice == 5:
        obj1.delete_beg()
    elif choice == 6:
        obj1.delete_end()
    elif choice == 7:
        x = int(input("Enter node to be deleted: "))
        obj1.del_byVal(x)
    elif choice == 8:
        obj1.printLL()
    elif choice == 9:
        obj1.printLLReverse()
    elif choice == 10:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
