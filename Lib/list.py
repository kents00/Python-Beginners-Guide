# What is List?
# List are a collection of data that are normally related to each other.
# Instead of storing into a different variables, we can store them into a list
# For example

Shelves = ["Book_1", "Book_2", "Book_3"]
print(Shelves)

# Note : For storing a list we use a square brackets "[]" when declaring a list.
# Multiple values are stored in separated by comma " , "

# We can also declare an empty list, and using a " .append() " we can add items to our list

Empty_list = []
Empty_list.append("New item")
print(Empty_list)

# Individual items in the list are accessible by their indexes

Collection = ["Apple", "Orange", "Bees"]
print(Collection[0])

# Note : The item indexes are start at ZERO, not ONE

# Accessing last index to start

Reversed_Item = ['One', 'Two', 'Three', 'Last Item']
print(Reversed_Item[-1])

# Accessing range of indexes
# To specify a range of indexes we will use slice " : "

Range_Indexes = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(Range_Indexes[2:6])

# You notice that it access the list 'cherry' up to 'melon'
# Note : Remember that we start 0,1,2,3,4,5,6... the item in the start indexes is always included but the last item is always excluded

# Slice notation includes a third number known as ' stepper '

Stepper_Index = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(Stepper_Index[1:5:2])

# Notice we get a sub consisting of every second number from index 1 to index 5-1 because the stepper is 2

# Slice notations have a useful defaults The default for the first number is zero, and the default for the second number is size of the list being sliced. 
# For example

Index_slice = ["One", "Two", "Three", "Four", "Five"]
print(Index_slice[:4])

# It gives us a values from index 0 to index 4-1

Index_slice = ["One", "Two", "Three", "Four", "Five"]
print(Index_slice[1:])

# It gives us a values from index 1 to index 5-1 