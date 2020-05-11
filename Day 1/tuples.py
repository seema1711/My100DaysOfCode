''' A tuple is a sequence of immutable Python objects.
Tuples are sequences, just like lists, but 
tuples can't be changed unlike lists & tuples
use parentheses, whereas lists use square brackets'''

### CREATING TUPLE ###
tup1=('physics','chemistry',1997,2000)
tup2=(1,2,3,4,5)
tup3="a","b","c","d"

### CREATING AN EMPTY TUPLE ###
tup4=()

### CREATING A SINGLE VALUED TUPLE ###
tup5=(50,) # You have to use comma, even though it contains only a single value

### ACCESSING VALUES IN TUPLES ###
print("tup1[1]: ",tup1[1])
print("tup2[1:3]: ",tup2[1:3])

### UPDATING TUPLES ###
''' Tuples are immutable which means you can't
update or change the values of tuple elements.
But if you want to do that, you can use type casting 
i.e. changing the tuple into a list and then updating the value of it
and again type cast back to tuple. But it is not recommended to do that.
'''
tup4=tup1+tup2
print("tup4: ",tup4)

### DELETE TUPLE ELEMENTS ###
''' Removing individual tuple is not possible.
There is, ofcourse, nothing wrong with putting 
another tuple with the undesired elements discarded.
To explicitly remove an entire tuple, use "del" statement.
'''
del tup4
print("after deleting tuple 4: ",tup4)

''' Basic tuple operations include the following ->
1. lenth: len((1,2,3)) => Output-- 3
2. Concatenation: (1,2,3) + (4,5,6) => Output-- (1,2,3,4,5,6)
3. Repitition: ('Hi',)*3 => Output-- ('Hi','Hi','Hi')
4. Membership: 3 in (1,2,3) => Output-- True
5. Iteration: for x in (1,2,3):
                print(x)
            Output-- 1 2 3
'''



