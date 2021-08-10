str1 = "Hello world!"
yr = 2021
a, b = 4, 6  # you can define multiple variable in single line.
print(str, yr)
x = "{}{}".format("test ", 123)
print(x)
print(a, b)
print(type(a))

# data types are int, string, list, tuple and dictionary.
# list is the collection of different data type and the elements are changeable.
# list has square bracket.
lis = [4, "string element", 7.86, 56, "check", "last"]
print(lis)
print(lis[1])
print(lis[-1]) # to print last element
print(lis[2:5]) # range works as n:n-1
lis.insert(1, 25) # to add new element in the list (position, value)
print(lis)
lis.append(100) # to add element at last of the list
print(lis)
lis[2] = "Changed element" # to change the element in the list
print(lis)
del lis[6] # to delete the element from the list
print(lis)

# you cannot change element in tuple data type rest is same as list
# tuple uses round bracket
tup = ("first", 45, 2.36, "check", 89)
print(tup)
print(tup[2])

# dictionary works on key:values pair
# in dictionary value print on the key basis not on index basis.
# it uses the curly brackets
dic = {"first": "Rahul", "age": 23, 7: "Number", 0: 1}
print(dic)
print(dic["first"])
print(dic[7])
print(dic[0])
# adding values to dictionary in run time
dic["lastname"] = "Singh"
print(dic)
dic[5] = 51
print(dic)
