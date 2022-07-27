# Function and Modules

# What are Functions?
# Functions are a way to group a series of statements together to perform a specific task.
'''
Depending on how the function is written, whether it is part of a class (a
class is a concept in object-oriented programming which we will not cover
in this book) and how you import it, we can call a function simply by
typing the name of the function or by using the dot notation. Some
functions require us to pass data in for them to perform their tasks. These
data are known as parameters and we pass them to the function by
enclosing their values in parenthesis ( ) separated by commas.

For instance, to use the print() function for displaying text on the
screen, we call it by typing print(“Hello World”) where print is
the name of the function and “Hello World” is the parameter.

'''

# Defining Your Own Functions
# To define a function, we use the keyword def followed by the name of the function.
# The function body is enclosed in round brakets.
# Example

from email import message


def my_function():
     print("Hello from a function")
#
# Calling a Function
# To call a function, we use the name of the function followed by the parenthesis.
# Example

my_function()

# Parameters
# A function can take in parameters. These parameters are known as arguments.
# Example

def Add(a, b):
    print(a + b)

Add(5, 6)

# Return Value
# A function can return a value. This value is known as the return value.
# Example

def Add(a, b):
    return a + b

print("The sum of 10 and 11 is: ", Add(10,11))

# Difference between return and print
# The return statement is used to return a value from a function.
# The print statement is used to display text on the screen.
# Example

def Greeting():
    print("Hello World")

def Greet():
    return "Hello World"

Greeting()
print(Greet())

# The pass Statement
# The pass statement is used when a statement is required syntactically but you do not want any code to execute.
# Example

def Nop():
    pass

Nop()

# The Global Statement
# The global statement is used to modify the value of a variable that is declared outside of a function.
# Example

def Global_Example():
    global x
    x = 10
    print(x)

Global_Example()

# The Nonlocal Statement
# The nonlocal statement is used to modify the value of a variable that is declared inside a function.
# Example

def Nonlocal_Example():
    x = 10
    print("This is Nonlocal_Example")
    def Local_Example():
        nonlocal x
        x = 20
        print(x)
        print("This is Local_Example")
    Local_Example()
    print(x)

Nonlocal_Example()

# The Lambda Expression
# The lambda expression is used to create a function that can be passed as an argument to another function.
# Example

def Lambda_Example(x):
    print("This is a lambda expression")
    return lambda y: x + y

print(Lambda_Example(10)(20))

# The Map Function
# The map function is used to apply a function to each item in a list.

def Map_Example(x):
    return x * 2

print(Map_Example(10))

# The Filter Function
# The filter function is used to apply a function to each item in a list and return a list of items for which the function returned True.

def Filter_Example(x):
    return x > 5

print(Filter_Example(10))

# The Reduce Function
# The reduce function is used to apply a function to each item in a list and return a single value.

def Reduce_Example(x):
    return x + 10

print(Reduce_Example(15))


# Variable Scope
# The scope of a variable is the part of the program where the variable is defined.
# There are two types of scopes: local and global.

# Local Scope
# Any variable declared inside a function is only accessible within the function. These are known as local variables.

# Global Scope
# Any variable declared outside of a function is accessible within any function. These are known as global variables.

# Example Local Scope
def Local():
    x = 10 # This will print the local variable x
    print(x)

# Nested Local Scope Function 
def Local_01():
    x = 10
    def Local_02(): # The local variable can be accessed from a function within the function
        print(x)
    Local_02()

# Example Global Scope
x = 10
def Global():
    print(x) # Anyone can access the global variable x

Global()


c = 100
def Global_01():
    c = 90
    print(c)

Global_01() # This will prinnt local variable c (90)
print(c) # This will print global c (100)

# Example Giving an Errors 

This_is_global = "This is global"

def Local_scope():
    This_is_local = "This is local"
    print(This_is_local)
    print(This_is_global)

print(This_is_local) # This will give an error because this_is_local is not defined as a global variable
Local_scope()