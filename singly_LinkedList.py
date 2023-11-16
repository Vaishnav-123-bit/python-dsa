#singly linked list
class Node:
  def __init__(self,data):
    self.data=data;
    self.next=None;

class LinkedList():
  def __init__(self):
    self.head=None;

  def printLL(self):
    if self.head is None:
      print("emty list ")
    else:
      n=self.head;
      while n is not None:
        print(n.data,"-->",end=" ");
        n=n.next;


  def addBegining(self,data):
    newNode=Node(data);
    newNode.next=self.head;
    self.head=newNode;

  def add_end(self,data):
    newNode=Node(data);
    if self.head is None:
      self.head=newNode;
    else:
      n=self.head;
      while n.next is not None:
        n=n.next;
      n.next=newNode;

  def add_after(self,data,x):
    newNode=Node(data)
    n=self.head;
    while n.next != None:
      if n.data==x:
         break;
      n=n.next;
    if n is None:
      print("Node is not present in list")
    else:
      newNode.next=n.next;
      n.next=newNode;
  
  def add_before(self,data,x):
    if self.head is None:
      print("empty ll");
      return 
    if self.head.data==x:
      newNode=Node(data);
      newNode.next=self.head;
      self.head=newNode;
      return
    n=self.head;

    #while loop to get previous node of required node
    while n.next is not None:
      if n.next.data==x:
        break;
      n=n.next

    if n.next is None:
      print("element not in list")
    else:
      newNode=Node(data)
      newNode.next=n.next;
      n.next=newNode;

  def del_beg(self):
    if self.head==None:
      print("empty list")
    else:
      self.head=self.head.next;

  def del_end(self):
    if self.head==None:
      print("empty")
    elif self.head.next ==None:
      self.head=None;
      
    else:
      n=self.head
      while n.next.next is not None:
        n=n.next
      n.next=None;

  def del_anywhere(self,x):
    if self.head is None:
      print("cannot delete from empty LL")
      return
    if x==self.head.data:
      self.head=self.head.next;
      return;

    #search for previous node   
    n=self.head;
    while n.next is not None:
       if x==n.next.data:
        break
       n=n.next;
    if n.next is None:
      print("element not found")
    else:
      n.next=n.next.next

ll1=LinkedList();
while True:
  print("\nenter choice 1.Add beg 2.Add end 3.Add before 4.Add After 5.del beginning 6.delete end 7.Delete anywhere 9.PrintLL ")
  choice=int(input("enter choice"))
  if choice==1:
    data=int(input("data"))
    ll1.addBegining(data)
  elif choice ==2:
    data=int(input("data"))
    ll1.add_end(data)

  elif choice==3:
    data=int(input("data"))
    x=int(input("add before elemet .. "))
    ll1.add_before(data,x)
  elif choice==4:
    data=int(input("data"))
    x=int(input("add after elemet .. "))
    ll1.add_after(data,x)
  elif choice==5:
    ll1.del_beg()
  elif choice==9:
    ll1.printLL()
  elif choice==6:
    ll1.del_end()
  elif choice==7:
    x=int(input("enter element to be deleted"))
    ll1.del_anywhere(x)1
  else:
    break


