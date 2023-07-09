# Lists, tuples, and set (Python 3.10)
# This coding exercise requires you to complete three steps:

# Create a list, called my_list , with three numbers. The total of the numbers added together should be 100.

# Create a tuple, called my_tuple , with a single value in it

# Modify the variable set2  so that set1.intersection(set2)  returns {5, 77, 9, 12} 

# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.

# Create a tuple, called my_tuple, with a single value in it

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5}

#############################################################################################################################################

# Flow control—loops and ifs (Python 3.10)
# This coding exercise has two steps.

# 1.Modify the code so that the evens list contains only the even numbers of the numbers list. You do not need to print anything.

# 2.For part 2, add a clause to the if statement such that if the user's input is "q", your program prints "Quit".

# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
evens.append(number)


# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")

#############################################################################################################################################