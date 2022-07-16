# Tuple
# Tuple are just like a list, but you cannot modify their values
# The initial values are the values that will stay for the rest of the program
# For example

Tuple_months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
print(Tuple_months)

# Accessing tuple items 
# Tuple items are indexes, the first item index [0]... and so on

print(Tuple_months[0])

# Tuple items can access last item to first 

print(Tuple_months[-1])

# Range of Indexes 
# Tuple can be also access range of index, similar to list

print(Tuple_months[0:5])

# Note : It print only the first item and the last is excluded

# Accessing the last item to first using range indexes

print(Tuple_months[-11:-5])

# Note: tuples are in ordered,  it means that the items have a defined order, and that order will not change.
# Note: tuples are unchangeable, it means that you cannot modify nor add and remove items after the tuple has been created

# Note : tuples allow duplicates, since the tuples are indexed, they can make items with the same values
Tuples_duplicates = ('One', 'One' , 'Two', 'Two', 'Three', "Four", "Five", "Six", "Seven")
print(Tuples_duplicates)