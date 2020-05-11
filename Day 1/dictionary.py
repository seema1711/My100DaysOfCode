''' In dictionary each key is separated from it's 
value by a colon, the items are separated by commas,
and the whole thing is enclosed in curly braces.
'''
### TO CREATE AN EMPTY DICTIONARY ###
emptyDict={}
print(emptyDict)

''' Keys are unique within a dictionary while 
values may not be. The value of a dictionary can
be of any type, but the keys must be of an immutable
data type such as strings, numbers, or tuples.
'''
### ACCESSING VALUES IN DICTIONARY ###
dict1={'Name':'Seema','Age':21,'Hobby':'Dancing'}
print("dict1['Name']: ",dict1['Name'])
print("dict1[Age]: ",dict1['Age'])

### UPDATING DICTIONARY ###
''' You can update a dictionary by adding a new
entry or a key-value pair, modifying an existing
entry, or deleting an existing entry as shown
'''
dict1['Age']=20 #updating existing entry
print("Updated dictionary: ",dict1)

### DELETE DICTIONARY ELEMENTS ###
''' You can either remove individual dictionary
elements or clear entire contents of a dictionary.
You can also delete the entire dictionary in a single
operation. 
'''
del dict1['Name'] #remove entry with key 'Name'
dict1.clear() #remove all entries in dict1
del dict1 #delete entire dictionary

#print(dict1)

### DUPLICATE KEYS ###
''' When duplicate keys are encountered during 
assignment, the last assignment wins.
'''
dict2={'Name':'Seema','Age':21,'Name':'Aakanksha'}
print("dict2['Name']: ",dict2['Name'])

### KEYS MUST BE IMMUTABLE ###
''' Which means you can use strings, numbers, tuples
as dictionary keys but something like ['key'] is not
allowed.
'''
dict3={['Name']: 'Seema','Age':21}
print(dict3)




