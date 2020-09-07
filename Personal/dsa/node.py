# Node class
class node:
    def __init__(self, value):
        self.value = value
        self.next = None
    # printing the node
    def PrintNode(self):
        print(self.value)

# linked list class
class linkedlist:
    def __init__(self):
        self.head = None

    def add(self, val):
        newNode = node(val)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
    
    def PrintLL(self):
        if self.head is None:
            raise IndexError("There is nothing in the linkedlist")
        else:
            current = self.head
            while current != None:
                print (current.value)
                current = current.next


nodes = node(10)

ll = linkedlist()
ll.add(5)
ll.add(5)
ll.add(5)
ll.add(5)
ll.add(5)
ll.PrintLL()
