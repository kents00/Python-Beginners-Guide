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


# List operations 

# append()
# Append method can add a single element at a time

List_append = []
List_append.append("Append to the list")
print(List_append)

# extend()
# extend method is used to add more than one element at the end of the list 

List_extend = ["One", "Two", "Three", ]
List_extend.extend(["Extend apple", "Extend the time!"])
print(List_extend)

# insert()
# insert method can add an element at a given index/position in the list
# This method takes 2 arguments
# The 1st argument specifies the position, and the 2nd argument specifies the element to be inserted

List_insert = ['One', 'Teo', 'Three']
List_insert.insert(3, "Hello")
List_insert.insert(0, "First Item!!")
print(List_insert)

# remove()
# remove method is used to remove an element to the list

List_remove = ["One", "Two", "Three", "Remove this one!"]
List_remove.remove("Remove this one!")
print(List_remove)

# pop()
# pop method can remove an element from any position in the list

List_pop = ['One', 'Two', 'Three', "Four", "Pop this!" ,"Five"]
List_pop.pop(4)
print(List_pop)

# slice()
# slice method is used to print a section in the list

List_slice = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(List_slice[:4])  # prints from beginning to end index
print(List_slice[2:])  # prints from start index to end of list
print(List_slice[2:4]) # prints from start index to end index
print(List_slice[:])   # prints from beginning to end of list

# reverse()
# reverse method is used to reverse the elements of the list 

List_reverse = ['One', 'Two', 'Three', "Four", "Five", "Segggss!"]
List_reverse.reverse()
print(List_reverse)

# len()
# len method is to return the length of the list, * Number of the elements

List_len = ['One', 'Two', 'Three', "Four", "Five", "Segggss!", "Seven"]
print(len(List_len))

# min() and max()
# min method returns the minimum value of the list
# max method returns the maximum value of the list

List_minmax = ['One', 'Two', 'Three', "Four", "Five", "Segggss!", "Seven"]
print(min(List_minmax))
print(max(List_minmax))

# count()
# count method returns number of occurrences of a given element of the list

List_count = ["One", "Two", "Three", "Four", "This will count as one","This will count as one", "This will count as one"]
print(List_count.count("This will count as one"))

# concatenate()
# concatenate method is used to merge a list, returning a single list

List_concatenate_1 = ["This is concatenate_1 will be merged by"]
List_concatenate_2 = ["Concatenete_2 totally merged by concatenate_1"]
print(List_concatenate_1+List_concatenate_2)

# multiply()
# multiply method is used to multiply the list in 'n' times

List_multiply = ["Multiplying by items"]
print(List_multiply*3)

# index()
# index method return the position of the occurrence of the given element
# index takes two optional parameters- the begin index and the end index

List_index = ['One', 'Two', 'Three', "Four", "Five", "Segggss!", "Seven"]
print(List_index.index("One")) # Searching the whole list
print(List_index.index("One", 0, 2))

# sort()
# sort method used to sorts the list into ascending order

List_ascending = ['1','4','2','3']
List_ascending.sort()
print(List_ascending)

# clear()
# clear method used to clear all the elements inside the list

List_clear = ["This string will be erase shortly"]
print(List_clear.sort())
