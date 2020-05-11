''' We can remove an existing node using the key for that node. We will locate
the previous node of the node which is to be deleted. Then point to the next pointer
of this node to the next node to be deleted.
'''

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    def AtBeginning(self,data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
# Function to remove node
    def RemoveNode(self, Removekey):
        HeadVal = self.head
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            previous = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        previous.next = HeadVal.next
        HeadVal = None
    def listprint(self):
        printval = self.head
        while (printval):
            print(printval.data)
            printval = printval.next

list = SLinkedList() 
list.AtBeginning('Seema')
list.AtBeginning('Kareena')
list.AtBeginning('Salman')
list.AtBeginning('Akshay')
list.AtBeginning('Preeti')
list.RemoveNode('Preeti')
print("After removing the node")
list.listprint()
