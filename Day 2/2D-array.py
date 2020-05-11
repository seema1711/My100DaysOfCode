### ACCESSING VALUES IN a 2D-ARRAY ###
''' The data elements in 2D arrays can be accessed using two indices.
One index = referring to the main or parent array
Second index = referring to the position of the data element in the inner array.

If we mention only one index then the entire inner
array is printed.
'''
from array import array
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(A[0])
print(A[1][2])

### HOW TO PRINT ENTIRE 2D-ARRAY ###
print("Printing entire 2D-array")
for r in A:         # r = row, c = column
    for c in r:
        print(c,end=" ")
    print()

### INSERTING VALUES IN 2D-ARRAY ###
print("Inserting values to 2D-array")
A.insert(1,[-1,-2,-3,0])
for r in A:         # r = row, c = column
    for c in r:
        print(c,end=" ")
    print()

### UPDATING VALUES IN 2D-ARRAY ###
A[2] = [11,45]
A[0][3] = 7
print("After updating the 2D-array")
for r in A:         # r = row, c = column
    for c in r:
        print(c,end=" ")
    print()

### DELETING THE VALUES IN 2D-ARRAY ###
del A[3]
print("After deleting 2D-array")
for r in A:         # r = row, c = column
    for c in r:
        print(c,end=" ")
    print()

