# dictionary 
# Dictionary items are ordered, changeable, and does not allow duplicates.
# dictionary is a collection of a related data Pairs.
# For example,  we want to store a name and their ages of the users

Dic_names = {"Johnny":15, "Nick":10, "Aiko": 11}
print(Dic_names)

# Note: We cannot declare a same dictionary key twice
# It returns only the last item in the dictionary

Dic_error = {"Error": 10, "Error":11}
print(Dic_error)

# Accessing Dictionary Items

Dic_Library = {
    "Phone_Number" : "012345",
    "Model" : "Phone_01",
    "Year" : "2022"
}
print(Dic_Library["Phone_Number"])

# We can also use get() to get the same result

Get_function = Dic_Library.get("Model")
print(Get_function)

# keys() method will return a list of all keys in dictionary

Get_keys = Dic_Library.keys()
print(Get_keys)

# Dictionaries are defined as objects with the data type 'dict'

Dic_type = {
    "Dictionary" : "This is a dictionary"
}
print(type(Dic_type))

# To determine the length of a dictionary

Dic_len = {
    "Length" : "Prints only the keys",
    "Length01" : "It will never prints the values of their keys"
}

print(len(Dic_len))

# values() method return a list of all values in the dictionary

Dic_all = {
    "Colors" : ["Red", "Blue", "Indigo"], 
    "Golds" : "24karat"
}

print(Dic_all.values())

# items() will return each item in dictionary, as tuples in a list

Dic_itm = {
    "This is an item" : "Value of this item",
    "Item01" :  "Apple"
}

print(Dic_itm.items())

# Checking if the key is present in the dictionary

Dic_chk = {
    "Brand" : "Brand of the phone",
    "Year" : "Year of manufacturers created this phone",
    "Model" : "Model of the phone"
}

if "Year" in Dic_chk:
    print("Yes!, The Year of the manufacturers list this Dictionary")

# Declaring data in strings and numbers

Dic_rdm = {
    1.5 : "One",
    "Two" : 2.5,
    3 : "+",
    4.5 : 5
}

print(Dic_rdm)

# Note that items in a dictionary are not stored in the same order as the way you declare them.

# Changing value of keys in dictionary

Dic_rdm["Two"] = 2.9999
print(Dic_rdm)