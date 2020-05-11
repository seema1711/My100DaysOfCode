''' Mathematically a set is a collection of items not in any particular order.
Rules for Sets in Python:
1. The elements in the set can't be duplicates.
2. The elements in the set are immutable but the set as a whole is mutable.
3. There is no index attached to any element in a Python set. So, they don't support any indexing or slicing operation.

Operations that can be performed by Sets in Python-
1. Union
2. Intersection
3. Difference
4. Complement etc.
'''

### CREATING A SET ###
''' We can create sets by two methods'''

Days=set(['Mon','Tues','Wed','Thu','Fri','Sat'])
Months={'Jan','Feb','Mar'}
Dates={17,13,23}
print(Days)
print(Months)
print(Dates)

### ACCESSING VALUES IN SET ###
print("Days in a week: ")
for d in Days:
    print(d)

### ACCESSING ITEMS TO A SET ###
print("Adding Sun to set Days")
Days.add("Sun")
print(Days)

### REMOVING ITEM FROM A SET ###
print("Removing Sun from Days set")
Days.discard('Sun')
print(Days)

### UNION OF SETS ###
DaysA = {'Mon','Tues','Sun'}
DaysB = set(['Wed','Thu','Fri','Sat'])
AllDays = DaysA | DaysB
print("Union of the days of the week: \n", AllDays)

### INTERSECTION OF SETS ###
AllDays = DaysA & DaysB
print("Intersection of the days of the week: \n", AllDays)

### DIFFERENCE OF SETS ###
AllDays = DaysA - DaysB
print("Difference of the days of the week: \n", AllDays)

### COMPARE SETS ###
DaysA = {'Mon','Tues','Wed'}
DaysB = {'Mon','Tues','Wed','Thu','Fri','Sat','Sun'}
Subset = DaysA <= DaysB
Superset = DaysA >= DaysB
print(Subset)
print(Superset)






