#stack using list

stack=[]
stack.append(10)
stack.append(20)

stack

stack.pop()
stack
len(stack)==0




#stacking implementation using list 
stack=[]
def push():
  if len(stack)==n:
    print("stack is full")
  else:
    element=int(input("enter"))
    stack.append(element)
    print(stack)
def pop():
  if not stack:
    print("empty stack")
  else:
    e=stack.pop()
    print("element removed",e)
    print(stack);
    
n=int(input("enter stack limit"))
while True:
  print("1.push \t2.pop \t3.quit")
  cho=int(input("enter choice"))
  if cho==1:
    push();
  elif cho==2:
    pop();
  else:
    break;



#stack using class

class Xstack:
  def createStack(self,size):
    self.maxSize=size;
    self.tos=-1
    self.stack=[];
  def isFull(self):
    if self.tos==self.maxSize-1:
      return True
    else:
      return False
  def push(self,e):
    if self.tos==self.maxSize-1:
      print("full stack") 
    else:
      self.tos+=1;
      self.stack.append(e) 
  
  def pop(self):
    if self.tos==-1:
      print("empty stack");
    else:
      self.tos-=1
      e=self.stack.pop()
      print("element removed ",e);

  def display(self):
    for i in range(self.tos,-1,-1):
      print(self.stack[i])

obj=Xstack();
obj.createStack(5);

while True:
  print("enter choice : 1push \t 2pop \t 3display")
  choice=int(input("choice ?"))   
  if choice==1:
    e=int(input("enter num"))
    obj.push(e);
  elif choice==2:
    obj.pop()
  elif choice==3:
    obj.display()
  else:
    break





