class Person(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        return "Hello my name is " + self.name

name = input()
age = input()
person1 = Person(name, age)
print(person1.myfunc())
