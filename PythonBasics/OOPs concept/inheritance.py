from constructor_variables import second_class


class child_class(second_class):
    num2 = 200

    def __init__(self):
        second_class.__init__(self, 2, 10)

    def getAllData(self):
        return child_class.num2 + self.num + self.addition()


obj = child_class()

print(obj.getAllData())
