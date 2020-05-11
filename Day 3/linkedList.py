''' A Linked List is a sequence of data elements, which are connected together via links.
Each data element contains a connection to another data element in form of a Pointer.
Python doesn't have LL(Linked List) in its standard library. I will implement the concept of LL 
using the concept of nodes, for which we have to create a node class.

I will cover -
~ Singly LL => DS in which there is only one link between any 2 data elements.
'''

### CREATING A LL ###
''' A LL is created by using the node class. We create a Node object and create another class to use this node object.
We will pass the appropriate values through the node obj to point to the next data elements.
'''
class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Print the linked list
    
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtBeginning(self,newdata):
            NewNode = Node(newdata)
# update the new nodes next val to existing node
            NewNode.nextval = self.headval
            self.headval = NewNode

list1 = SLinkedList()
list1.headval = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')
# Link first node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

### TRAVERSING A LL ###
''' Singly LL can only be traversed in only forward direction starting from the first data
element. We print the value of the next data element by assigning the pointer of the next node
to the current node.
'''
print("Traversing a LL")
list1.listprint()

### INSERTION IN A LL ###
''' Inserting element in a LL involves reassigning the pointers from the existing nodes to the newly
inserted node. Depending on whether the new data element is getting inserted at the beginning or at the 
middle or at the end of the LL.
'''
# 1. Inserting at the beginning of the LL
''' This involves pointing the next pointer of the new data node to the current head of the LL. So, 
the current head of the LL becomes the second data element and the new node becomes the head of the LL.
'''
list2 = SLinkedList()
list2.headval = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')

list2.headval.nextval = e2
e2.nextval = e3
list2.AtBeginning('Sun')
print("Insertion at the beginning of the LL: ")
list2.listprint()






