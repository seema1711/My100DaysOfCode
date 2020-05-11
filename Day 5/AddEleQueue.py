<<<<<<< HEAD
### ADDING ELEMENTS TO A QUEUE ###
class Queue:
    def __init__(self):
        self.queue = list()
    def add(self,dataval):
    # Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
    def size(self):
        return len(self.queue)

TQueue = Queue()
TQueue.add('Taj1')
TQueue.add('Taj2')
TQueue.add('Taj3')
TQueue.add('Taj4')
print(TQueue.size())

=======
### ADDING ELEMENTS TO A QUEUE ###
class Queue:
    def __init__(self):
        self.queue = list()
    def add(self,dataval):
    # Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
    def size(self):
        return len(self.queue)

TQueue = Queue()
TQueue.add('Taj1')
TQueue.add('Taj2')
TQueue.add('Taj3')
TQueue.add('Taj4')
print(TQueue.size())

>>>>>>> 3ab12aa2dd515dac2d001ccb20fcb678b9842d4a
        