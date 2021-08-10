class first_class:

    num = 101  # syntax for creating variable in class

    def getData(self):
        print('I am executing as a method in class')

# this is the syntax, to create object of the class in python
obj = first_class()

obj.getData()
print(obj.num)
# OR
x = obj.num
print(x)

