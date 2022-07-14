# Escape Characters
# Sometimes we need to print the "unpritable" characters such as tab or a newline.
# So python created a keywords for that these are the following:

# \' ( Single Quote )
print("It\'s gonna be fun!")

# \\ ( Backslash )
print("Only inserts one \\ backslash.")

# \n ( Newline )
print("New\nLine")

# \r ( Carriage Return ) * kinda similar to Newline
print("You learn, \r alot!")

# Note : If you do not want characters preceded by the \ character to be interpreted as special characters, you can use raw strings by adding an r before the first quote. For instance, if you do not want \t to be interpreted as a tab, you should type print (r‘Hello\tWorld’). You will get Hello\tWorld as the output

# \t ( Tab )
print("Make's an extra \t space!")

# \b ( Backspace )
print("Deletes \bextra \bspace ")

# \f ( Formfeed )
print(" Creates new \fline with an tab")

