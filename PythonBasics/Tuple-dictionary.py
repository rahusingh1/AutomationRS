# list and tuple data types are same
# but tuple data type is immutable means it is not editable once an element is added in the tuple.
# you cannot change the existing behaviour
# list has square bracket but tuple has normal bracket/parentheses

tuple1 = (5, 7.62, 'rahul', 78)

print(tuple1)

print(tuple1[1])

# Dictionary: it is simply the key value data type
# based on the type you can use quotes like if key is string and value is integer then "a":4 and vice-versa
# dictionary print the values based on the keys not on indexes

dic = {1: "rahul", "a": 45, "b": "Hellow world", 4: 23}

print(dic['a'])

print(dic[4])

# adding new values to dictionary on run time

dict = {}

dict["FirstName"] = "Rahul"

dict["LastName"] = "Singh"

dict["Gender"] = "Male"

dict[9] = 11

print(dict)
print(dict[9])