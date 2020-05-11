<<<<<<< HEAD
class Queue:
    def __init__(self):
        self.queue = list()
    def add(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
# Pop method to remove elements
    def removefromque(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "No elements in the queue"

PQueue = Queue()
PQueue.add('Sim1')
PQueue.add('Sim2')
PQueue.add('Sim3')
PQueue.add('Sim4')
print(PQueue.removefromque())
print(PQueue.removefromque())
=======
class Queue:
    def __init__(self):
        self.queue = list()
    def add(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
# Pop method to remove elements
    def removefromque(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "No elements in the queue"

PQueue = Queue()
PQueue.add('Sim1')
PQueue.add('Sim2')
PQueue.add('Sim3')
PQueue.add('Sim4')
print(PQueue.removefromque())
print(PQueue.removefromque())
>>>>>>> 3ab12aa2dd515dac2d001ccb20fcb678b9842d4a
