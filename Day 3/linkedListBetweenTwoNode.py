''' This involves changing the pointer of a specific node to point to the new node. That is possible by passing
in both the new node and the existing node after which the new node will be inserted. So, we will be defining an additional
class which will change the next pointer of the new node to the next pointer of the middle node. Then assign the new node to 
next pointer of the middle node.
'''
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add node
    def InBetween(self,middle_node,newdata):
        if middle_node is None:
            print("Node is absent")
            return
    
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

# Print the LL
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node('Seema')
node2 = Node('Shreya')
node3 = Node('Aakanksha')

list.headval.nextval = node2
node2.nextval = node3

list.InBetween(list.headval.nextval,'Sunny')
print("Insertion of nodes in between the LL")
list.listprint()