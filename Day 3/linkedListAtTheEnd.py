''' This involves pointing the next pointer of the current last node of the linked list to the 
new data node. So, the current last node of the linked list becomes the second last data node & 
the new node becomes the last node of the LL.
'''
### LINKED LIST INSERTION AT THE END ###
class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while (last.nextval):
            last = last.nextval
        last.nextval = NewNode

# Print the LL 
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node('Mon')
node2 = Node('Tue')
node3 = Node('Wed')

list.headval.nextval = node2
node2.nextval = node3

list.AtEnd('Thu')

print("Adding new element to LL at the end")
list.listprint()



