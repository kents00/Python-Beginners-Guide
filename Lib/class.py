# What is class?
'''
Classes are Object Oriented
an object's characteristics define
what are the distinguishing features,
It's like an blueprint for creating objects
'''
# Example for this is define what are the characteristics of an human

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is {} and I am {} years old".format(self.name, self.age))


Human("Makima", "21").greet()

# Why do we need to use __init__ method?
'''
When we create a class, we need to use the __init__ method to initialize the class.
This is because the __init__ method is called every time we create a new object.
'''