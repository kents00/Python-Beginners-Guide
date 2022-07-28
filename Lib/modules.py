# Modules
'''
Python comes with a large number of built-in functions. These functions
are saved in files known as modules. To use the built-in codes in Python
modules, we have to import them into our programs first. We do that by
using the import keyword. There are three ways to do it.
'''

# The first way is to use the import keyword.

# For instance, we can import the math module by using the following code:

import math

print(math.sqrt(25))

# Or you can assign a module with the name of the module to a variable:

import math as m

# The third method is to import specific functions from a module.

from math import sqrt, floor, ceil

print(math.floor(3.7))
print(math.ceil(3.7))

# Creating Your Own Modules
# To create your own modules, you can create a file with the .py extension.
# The file can contain any code you want.
# Example

# This is an example of importing modules into different folders:
from pymodules.sub_module import checkifPrime

answer = checkifPrime(11)
print(answer)