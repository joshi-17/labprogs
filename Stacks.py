class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack:
    def __init__(self):
        self.top=None
    def display(self):
        if self.top==None:
            print("Stack is empty")
        else:
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
            
            print("top of the stack is ",self.top.data)
    def push(self):   
        n=int(input("enter the no of elements  u want to insert: "))
        for i in range(n):
            x=int(input("Enter the element: "))
            new=Node(x)
            if self.top is None:
                self.top=new
                self.top.next=None
            else:
                new.next=self.top
                self.top=new
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            self.top=self.top.next
            
st1=Stack()
st1.push()
st1.display()
st1.pop()
st1.display()
