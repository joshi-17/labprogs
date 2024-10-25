class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LL:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref
            print("None")

    def addbeg(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def addend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def addbetween(self, data, x):
        c = 0
        if self.head is None:
            print("LL is empty and cannot be filled")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                c += 1
                break
            else:
                n = n.ref
        if c == 1:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        else:
            print("Element not found")

    def delbeg(self):
        if self.head is None:
            print("LL is empty and cannot be deleted")
        else:
            self.head = self.head.ref

    def delend(self):
        if self.head is None:
            print("LL is empty and cannot be deleted")
        else:
            n = self.head
            prev = None
            while n.ref is not None:
                prev = n
                n = n.ref
            if prev is None:
                self.head = None  # If there was only one node
            else:
                prev.ref = None

    def delbetween(self, x):
        c = 0
        prev = None
        if self.head is None:
            print("LL is empty and cannot be deleted")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                c += 1
                break
            else:
                prev = n
                n = n.ref
        if c == 1:
            if prev is None:  # If we are deleting the head
                self.head = n.ref
            else:
                prev.ref = n.ref
        else:
            print("Deletion is not possible")

def menu():
    print("\nMenu:")
    print("1. Add node at the beginning")
    print("2. Add node at the end")
    print("3. Add node between")
    print("4. Delete node from the beginning")
    print("5. Delete node from the end")
    print("6. Delete a specific node")
    print("7. Print linked list")
    print("8. Exit")

if __name__ == "__main__":
    ll = LL()
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter data to add at the beginning: "))
            ll.addbeg(data)
        elif choice == 2:
            data = int(input("Enter data to add at the end: "))
            ll.addend(data)
        elif choice == 3:
            data = int(input("Enter data to add: "))
            x = int(input("Enter the node data after which to add: "))
            ll.addbetween(data, x)
        elif choice == 4:
            ll.delbeg()
        elif choice == 5:
            ll.delend()
        elif choice == 6:
            x = int(input("Enter the data of the node to delete: "))
            ll.delbetween(x)
        elif choice == 7:
            ll.printLL()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
