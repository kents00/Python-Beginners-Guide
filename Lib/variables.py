# What are the variables?
# variables are names given data that can store anything like list, tuples and disctionaries
# To assign a variables we need a asignment sign "="
# for example
This_is_a_variable = 0
Thisisavariable = 0
ThisIsAVariable = 0
# Take note that the variables are case sensitive, so if the word is the same but the Letters are have are different (Lower_case and Upper_case) that means they are not the same

# Naming a Variables
# Naming a variables only contain (a-z, A-Z), number and underscores( _ )
# Take note that the first character should be a Letter(a-z, A-Z) not a Number(0-9) or else the variable will not read as a variable
# In addition, we cannot also use preassign words in python, or else that also cannot read as a variable.
# Also we will use a proper naming of the variable so that we can identify easily the assigned variable

# The Assignment Sign
# Assignment sign it means that we assign a variables 
# for example

x = 5
y = 10
x = y

print('x = ', x)
print('y = ', y)
# Notice the logic, x = 5 but if we run it i will be x = 10, But how??
# It is because the 'x' is assinging by the 'y', so the value of our x is 1 because we assign the x to y

#Next example, if we reverse the values of our variables

x = 10
y = 20
x = y

# Now we will add some logic
y = x

print('x = ', x)
print('y = ', y)

print('y = ', x)
# We notice the values of our x and y is change, it is because we reverse it and the value of x and y is 5
# In the third line i change the value of our y = x, and still printing the same value of the 5, but why??
# Is because the y is assigns to x ( y <- x) it becomes 5 while x remains unchanged.