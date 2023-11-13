#queue using list 
queue=[]
def enqueue():
  e=int(input("enter "))
  queue.append(e)
  print(queue);
def dequeue():
  if not queue:
    print("empty queue")
  else:
    e=queue.pop(0)
    print("elemet removed ",e)
    print(queue)

while True:
  print("1.enqueue \t2.dequeue \t3.quit")
  cho=int(input("enter choice"))
  if cho==1:
    enqueue();
  elif cho==2:
    dequeue();
  else:
    break;


#queue implementation using class:

class QueueImp:
  def createQueue(self,size):
    self.maxSize=size;
    self.rear=-1;
    self.front=-1;
    self.queue=[];
  def isFull(self):
    if self.rear==self.maxSize-1:
      return True;
    else:
      return False;
  
  def isEmpty(self):
    if self.front==self.rear:
      return True;
    else:
      return False;

  def enqueue(self,e):
    if self.isFull():
      print("Queue full")
    else:
      self.rear+=1;
      self.queue.append(e);
      print("elment added ",e)

  def dequeue(self):
    if self.isEmpty():
      print("queue is empty")
    else:
      item=self.queue[self.front]
      self.front+=1;
      if self.front>self.rear:
        self.front=self.rear=-1;
      
      print("elment reoved ",item)

  def display(self):
    if self.isEmpty():
      print("empty queue")
    else:
      for i in range (self.front,self.rear+1,1):
        print(self.queue[i])

obj=QueueImp()
obj.createQueue(5);
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)


obj.display()

obj.dequeue()
obj.dequeue()

obj.display()





