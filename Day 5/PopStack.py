<<<<<<< HEAD
''' We can only remove the top of the stack. We will
check the top element by calculating the size of the stack
first & then use the in-built pop() method to find out the top
element.
'''
class Stack:
    def __init__(self):
        self.stack = []
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    
    def remove(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop()

AddStack = Stack()
AddStack.add('Jan')
AddStack.add('Feb')
AddStack.add('Mar')
AddStack.add('Apr')
print(AddStack.remove())
print(AddStack.remove())
print(AddStack.remove())

=======
''' We can only remove the top of the stack. We will
check the top element by calculating the size of the stack
first & then use the in-built pop() method to find out the top
element.
'''
class Stack:
    def __init__(self):
        self.stack = []
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    
    def remove(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop()

AddStack = Stack()
AddStack.add('Jan')
AddStack.add('Feb')
AddStack.add('Mar')
AddStack.add('Apr')
print(AddStack.remove())
print(AddStack.remove())
print(AddStack.remove())

>>>>>>> 3ab12aa2dd515dac2d001ccb20fcb678b9842d4a
