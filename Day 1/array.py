from array import array
array1=array('i',[1,2,3,4,5])
print("basic python code")
### BASIC PYTHON CODE ###
for x in array1:
    print(x)

### ACCESSING ARRAY ELEMENT ###
print("accessing array element")
print(array1[3])

### INSERION OPERATION ###
array1.insert(1,60)
print("inserting element")
print(array1[1])
print(array1)

### DELETION OPERATION ###
array1.remove(3)
print("deleting element")
for x in array1:
    print(x)

### SEARCH OPERATION ###
print("searching an element")
print(array1.index(4))

### UPDATE OPERATION ###
array1[2]=8
print("updating array elements")
for x in array1:
    print(x)