class Node:
    def __init__(self,data):
        self.data=data
        self.pref=None
        self.nref=None
class DLL:
    def __init__(self):
        self.head=None
    def printDLL(self):
        if self.head is None:
            print("Dll is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.nref
    def printDLLREV(self):
        if self.head is None:
            print("DLL is empty")
        else:
            n=self.head
            while n is not None:
                n=n.nref
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.pref
    def addbeg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def addend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def addbetween(self,data,x):
        if self.head is None:
            print("Impossible to insert")
        else:
            new_node=Node(data)
            c=0
            n=self.head
            while n is not None:
                if n.data == x:
                    c+=1
                    break
                else:
                    n=n.nref
            if c==1:
                new_node.nref=n.nref
                n.nref=new_node
                new_node.pref=n
            else:
                print("Element not found")
    def delbeg(self):
        if self.head is None:
            print("Impossible to delete")
        elif self.head.nref is None:
            self.head=None
            print("DLL is empty after deleting")
        else:
            self.head=self.head.nref
            self.head.pref=None
    def delend(self):
        if self.head is None:
            print("Impossible to delete")
        elif self.head.nref is None:
            self.head=None
            print("DLL is empty after deleting")
        else:
            n=self.head
            prev=None
            while n.nref is not None:
                prev=n
                n=n.nref
            prev.nref=None
    def delbetween(self,x):
         if self.head is None:
            print("Impossible to delete")
         else:
             n=self.head
             c=0
             prev=None
             while n is not None:
                 if n.data ==x:
                     c+=1
                     break
                 else:
                     prev=n
                     n=n.nref
             if c==1:
                n.nref.pref=prev
                prev.nref=n.nref
             else:
                 print("element not found")
if __name__ == "__main__":
    dll = DLL()
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter data to add at the beginning: "))
            dll.addbeg(data)
        elif choice == 2:
            data = int(input("Enter data to add at the end: "))
            dll.addend(data)
        elif choice == 3:
            data = int(input("Enter data to add: "))
            x = int(input("Enter the node data after which to add: "))
            dll.addbetween(data, x)
        elif choice == 4:
            dll.delbeg()
        elif choice == 5:
            dll.delend()
        elif choice == 6:
            x = int(input("Enter the data of the node to delete: "))
            dll.delbetween(x)
        elif choice == 7:
            dll.printLL()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
