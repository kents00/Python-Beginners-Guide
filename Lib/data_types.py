# Data Types in Python
# In python we have three data types
# Integer ( int )
# Float ( float )
# String ( str )

# What is Integer?
# Integer are numbers that have no decimal parts
# Numbers like:
# -5, 10, 2, 0, -4, -7
# For example, we will assign a variables that contains Integers:

Integer_Number = 500
Score = 256

# What is Float?
# Float are the numbers that has a decimal parts
# Numbers like:
# 5.5, 6.9, 2.3, 4.7
# For example, we will assign a variables that contains Float:

Float_Number = 9.9
Liters = 1.5

# What is String
# String are refers to text
# We can declare a string by using :
# Single-qoutes ( ' )
# Double-qoutes ( " )

# We can add a two string by using a ( + ) sign
# For example

Word_1 = "I love "
Word_2 = "Python"
print(Word_1+Word_2)
# Or
Word_3 = "Python " + "Is great"
print(Word_3)

# Built-in String Functions

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

# To use a built-in function just type .function_name()
# For example
print('jonny' .upper())

# Formatting Strings using %
# String are formatted using the operator % 
# This gives you greater control over how you want your string to be displayed and stored.
# The syntax for using the % operator is

# " String to be formatted " % ( Values or variables to be inserted to the strings, separated by commas)

# The %s - represents the string
# The %d - represents the integer
# The %f - represents the float

# For example
Plaque = "COVID"
Total_deaths = 10
Put_your_mask = 5.5

Message = "%s is the most deadly plaque in historty over %d million deaths all over the world, wear your %s everytime!, You have %4.2f seconds to put your mask!" %(Plaque, Total_deaths, "Mask", Put_your_mask)
print(Message)

# If you want to add some spaces before the integer, we can add number between % and d
# % (number of spaces) d

print("%5d" %(123))
# This will give us 2 spaces in front in total length of 5

# In float 
# % (number of spaces) . (number of decimal places) d
print("%7.2f" %(1.244444444))
# This will give us a 2 decimal places, and 3 spaces in front and total length of 7

# Take Note: The strings are organized ( First come, First serve )
# Notice that these " %s, %d " are replaced by the variables, and the last one ("Mask") this is also a string so it also replace the last operator(%) in the line


# Formatting Strings using format()
# The syntax is :

# " String to be formatted " . format(values or variables to be inserted into the string, separated by commas )

# Note that we will never use ( %s, %d, %f ) this method
# Instead we will use the curly brackets {}

Message = 'The price of all goods have now increased by {0:d}, {1:s} increased by 150 to 200, the exchange rate is {2:4.2f}'.format(50, 'Chicken', 1.324312)
print(Message)

# The parameters are position in 0,1,2, whereas the first item will be stored in 0 and display where the first item is
# Then we will pass the second parameters: string, integers, and float 
# d, s, f 
# If the position of the item in invalid, for example
# We will choose the 0 which is 50 and we will pass a second parameter as a string
# It will throw and error that the number is integer and not a string
# For example

# Integer will never be a string(vice versa)
# Throws a error says the format code is integer not a string type 
Error_type = "This will throw and error {0:s}".format("This is a string type")
print(Error_type)

# If we change it to 's' which is string that would print the "This is a string type"

# Note: if you want a string type, you can simply remove the items on the curly brackets
Message = 'The price of all goods have now increased by {}, {} increased by 150 to 200, the exchange rate is {}'.format(50, 'Chicken', 1.324312)
print(Message)

# Type Casting
# What is type casting?
# Type casting is a know what are the functionalities and their limitations
# The three built-in functions allow us to do type casting these are:
# int(), floact(), str()

# Int
# int() function takes float or an appropriate string and converts it into integer
# For example

int(6.912243)
# This will return a int and remove those decimal places ( 6 )

int("9")
# Note : this is a string, but if the string is a integer that would be a integer type
# This will also return also a int ( 4 )

# Limitations
# The limitations in integers are strings and string + float
# For example

int("This is invalid")
# This will return error because integer dont accept string( Letters )

int("1.2999999")
# This is also return error because string + float 

# Float
# float() function takes only integer or an appropriate string and changes into a float.
# For example

float("5.33221")
# This is a float and not a string because quotation marks are removed

float("2") # or
float(2)
# This will return as a float type ( 2.0 )

# String
# str() converts integer and float into a string type
# For example

str(9.6)
# This will return as a string type ( "9.6" )

