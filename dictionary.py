my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)
print(my_dict['key1'])
prices_lookup = {'apple': 3.50, 'oranges':1.99,'chocolate':0.50, 'gum': 1.0}
print(prices_lookup['oranges'])
other_dictionary = {'k1': 123, 'k2': ['a','s','f'], 'k3':{'insideKey':100}}
print(other_dictionary)
print(other_dictionary['k3'])
print(other_dictionary['k3']['insideKey'])
print(other_dictionary['k2'][2])
print(other_dictionary['k2'][2].upper())
addToDictionary = {'k1':100, 'k2':200}
print(addToDictionary)
addToDictionary['k3'] = 300
print(addToDictionary)
addToDictionary['k1'] = 'NEW VALUE'
print(addToDictionary)
print(addToDictionary.keys())
print(addToDictionary.items())


