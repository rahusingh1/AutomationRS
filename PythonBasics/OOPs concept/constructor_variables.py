class second_class:

    num = 100

    # default constructor
    def __init__(self, a, b):
        self.first_num = a
        self.second_num = b
        print('i am called automatically when object is created')

    def getData(self):
        print('I am executing as a method in class')

    def addition(self):
        return self.first_num + self.second_num + second_class.num

obj = second_class(2, 4) # syntax to create object of the class in python
obj.getData()
x = obj.addition()
print(x)

obj2 = second_class(6, 8)
y = obj2.addition()
print(y)