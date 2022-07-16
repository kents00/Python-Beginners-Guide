'''
The comparison statement is the most common type of condition statement. 
We use the == symbol to compare whether two variables are the same. (double =) symbol For example, 
if you type x == y, you are asking the Check to see if the value of x equals the value of y. 
If this is the case, When the condition is met, the statement evaluates to True. Else,The assertion will be deemed False. 

'''

# The list below shows how these signs can be used and gives examples of statements that will evaluate to True.


5 != 2
5 > 2
2 < 5

5 >= 2
5 >= 5

2 <= 5
2 <= 2

# Three logical operators ( and, or, not )

# 'and'
# The operator returns True, if the conditions are met, Else it will return False
'''
TRUE AND TRUE = TRUE
TRUE AND FALSE = FALSE
FALSE AND TRUE = FALSE
FALSE AND FALSE = FALSE
'''
# Example

5 == 5 and 2 < 5 # returns True

10 != 2 and 5 > 4 # returns True

3 <= 1 and 9 == 8 # returns False

7 >= 9 and 1 <= 1 # returns False

# 'or'
# The operators returns True if at least one condition is met, Else it will return False.
'''
TRUE OR FALSE = TRUE
FALSE OR TRUE = TRUE
TRUE OR TRUE = TRUE
FALSE OR FALSE = FALSE
'''
# Example

5 == 5 or 5 < 2  # returns True

6 != 4 or 8 >= 3 # returns True

1 == 2 or 2 == 3  # return False

# 'not'
# The operators returns True if the condition after the 'not' keyword is False
'''
not FALSE = TRUE
not TRUE = FALSE
'''
# Example 

not 1 == 1 # returns False

not 2 >= 3 # returns True


# IF STATEMENT
# One of the most popular control flow statements is the if statement. 
# It enables the program to determine whether a certain condition has been met and to take the required action based on the outcome of the evaluation.
# Example

# If condtion 1 is met: do A
# Elif condition 2 is met: do B
# Else: do C

#condition_1 = str(input("Enter your name:"))
#condition_2 = int(input("Enter your age:"))

#if condition_1 == 'Kent' and condition_2 == 18:
#    print("Hello Kent!")
#elif condition_1 == 'Johnny' and condition_2 == 20:
#    print("Hello Johnny!")
#else:
#    print("You are not Kent nor Jhonny!")

# INLINE IF STATEMENT
# Inline if statement is used to evaluate a condition and take the required action based on the outcome of the evaluation.
# Example

sure = True
Inline = 'yes' if sure else 'no'
print(Inline)

print("This is a" if sure else "This is not a")

print("5 is greater than 2" if 5 > 2 else "5 is not greater than 2")

a = "Denji"
b = "Power"

print("%s may be a good doggo for Makima?" % ( a if b else "No"))

# For Loop
# For loop is used to iterate over a sequence of items, which is either a list, a tuple, a set, a dictionary, or a string.
# Example

List = [1, 2, 3, 4, 5]

for MyList in List:
    print(MyList)


List_1 = ["One", "Two", "Three", "Four", "Five"]

for MyList_1 in List_1:
    print(MyList_1)
    if MyList_1 == "Three":
        print("Three is the best!")
        break
