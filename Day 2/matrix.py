''' Matrix is a special case of 2D-array where each element is of strictly same size.
~ Every matrix is also a 2D-array but not vice versa. ~
'''

from numpy import *
arr = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])

mat=reshape(arr,(7,5))
print(mat)

### ACCESSING VALUES IN MATRIX ###
print("Accessing values in a matrix: ")
print(mat[2])
print(mat[0][1])

### ADDING A ROW ###
print("Adding a row: ")
mat_row=append(mat,[['Avg',12,15,13,11]],0)
print(mat_row)

### ADDING A COLUMN ###
print("After adding a column: ")
mat_col=insert(mat,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
print(mat_col)

### DELETING A ROW FROM A MATRIX ###
print("After deleting the 3rd row: ")
mat=delete(mat,[2],0) #delete(arr,obj,axis=None)
print(mat)

### DELETING A COLUMN FROM A MATRIX ###
print("Deleting a column from a matrix: ")
mat=delete(mat,s_[2],1)
print(mat)

### UPDATE A ROW IN A MATRIX ###
print("After updating a row: ")
mat[3]=['Thu',0,0,0]
print(mat)




