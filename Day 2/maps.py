''' Python maps also called ChainMap is a type of data structure to manage multiple dictionaries
together as one unit. The combined dictionary contains the key and value pairs in specific sequence 
eliminating any duplicate keys. 
The best use of ChainMap is to search through multiple dictionaries at a time and get the proper key-value
pair mapping. 
ChainMaps also behave as Stack data structure.
'''

### CREATING A CHAINMAP ###
'''If there are duplicate keys, then only the value from the first key is used. '''
import collections

dict1 = {'day1':'Mon','day2':'Tue'}
dict2 = {'day3':'Wed','day1':'Thu'}

result = collections.ChainMap(dict1,dict2)
# creating a single dictionary
print(result.maps,'\n')

print('keys = {}'.format(list(result.keys())))
print('Values = {}'.format(list(result.values())))
print()

# print all elements from the result
print('elements: ')
for key,val in result.items():
    print('{} = {}'.format(key,val))
print()

# find a specific value in the result
print('day3 in result: {}'.format(('day' in result)))
print('day4 in result: {}'.format(('day4' in result)))

### MAP REORDERING ###
result1 = collections.ChainMap(dict1,dict2)
print(result1.maps,'\n')

result2 = collections.ChainMap(dict2,dict1)
print(result2.maps,'\n')

### UPDATING MAP ###
dict2['day4'] = 'Fri'
print(result.maps,'\n')
