class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element   
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]
AddStack = Stack()
AddStack.add('Jan')
AddStack.add('Nov')
AddStack.peek()
print(AddStack.peek())
AddStack.add('Mar')
print(AddStack.peek())