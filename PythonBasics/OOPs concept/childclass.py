from constructor_variables import second_class

class child(second_class):
    num2 = 200

    def getfulldata(self):
        return self.num2 + child.num2

obj = child()

print(obj.getfulldata())