# This is an extension topic from modules.py:
# Which is creating modules and export them to other modules.

# If you want to store this module into different folders add __init__.py to the folder.
# This file is used to tell Python that this folder is a module.
# If you want to import this module, you can use the following code:
# from folder.filename import function/class/variable

def checkifPrime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    