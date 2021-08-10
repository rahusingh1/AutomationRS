# Data types in the python
# list is the collection of different data types
# list data type is immutable mean editable
list1 = [1, 2.56, 'rahul', {2, 5}, 34]

# To print list items
print(list1)

# to print a particular element from list
print(list1[1])

# to print last element from the list
print(list1[-1])

# to print multiple element in a sequence
print(list1[1:3])

# to add an element in the list at particular position
list1.insert(2, 'singh')
print(list1)

# to add an element in the end of the list
list1.append(86)
print(list1)

# to update the element in the list
list1[2] = "SINGH01"
print(list1)

# to delete the element from the list
del list1[5]
print(list1)
