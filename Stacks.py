class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class Stack:
    def __init__(self):
        self.top=None
    def display(self):
        if self.top==None:
            print("Stack is empty")
        else:
            n=self.top
            while n is not None:
                print(n.data)
                n=n.ref
            
            print("top of the stack is ",self.top.data)
    def push(self):   
        x=int(input("enter the no of elements  u want to insert: "))
        for i in range(x):
            y=int(input("Enter the element: "))
            new=Node(y)
            if self.top is None:
                self.top=new
                self.top.ref=None
            else:
                new.ref=self.top
                self.top=new
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            self.top=self.top.ref
            
st1=Stack()
st1.push()
st1.display()
st1.pop()
st1.display()
