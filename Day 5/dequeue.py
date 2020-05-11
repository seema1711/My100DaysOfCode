<<<<<<< HEAD
''' A double ended queue or Deque, supports adding and removing elements from either
end. The more commonly used Stacks and Queues are degenerate forms of deques, where the I/P
and O/P are fixed to one end.
'''
import collections
DoubleEnded = collections.deque(['Jan','Feb','Mar'])
DoubleEnded.append('Apr')

print("Appended to the right of the Deque")
print(DoubleEnded)

DoubleEnded.appendleft('Dec')
print("Appended to the left of the deque")
print(DoubleEnded)

DoubleEnded.pop()

print("Deleted from right")
print(DoubleEnded)

DoubleEnded.popleft()

print("Deleted from left")
=======
''' A double ended queue or Deque, supports adding and removing elements from either
end. The more commonly used Stacks and Queues are degenerate forms of deques, where the I/P
and O/P are fixed to one end.
'''
import collections
DoubleEnded = collections.deque(['Jan','Feb','Mar'])
DoubleEnded.append('Apr')

print("Appended to the right of the Deque")
print(DoubleEnded)

DoubleEnded.appendleft('Dec')
print("Appended to the left of the deque")
print(DoubleEnded)

DoubleEnded.pop()

print("Deleted from right")
print(DoubleEnded)

DoubleEnded.popleft()

print("Deleted from left")
>>>>>>> 3ab12aa2dd515dac2d001ccb20fcb678b9842d4a
print(DoubleEnded)