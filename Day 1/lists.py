### CREATING A LIST ###
list1=['physics','chemistry',1997,2000]
list2=[1,2,3,4,5]
list3=["a","b","c","d"]

### ACCESSING VALUES IN LISTS ###
print("list1[0] : ",list1[0])
print("list2[1:5] : ",list2[1:5])

### UPDATING LISTS ###
print("value available at index 2: ",list1[2])
list1[2]=2001
print("new value at index 2: ",list1[2])

### DELETE LIST ELEMENTS ###
print("present list: ",list3)
del list3[2]
print("after deleting value at index 2: ",list3)

