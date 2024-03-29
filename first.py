# name = "Bob"
# greeting = "Hello, Bob"

# print(greeting)

#List Tuple Set
# l = ["Bob", "Rolf", "Anna"] #if you do not have lists, then you'd have to define three variables
# t = ("Bob", "Rolf", "Anna") #you can not modify, add or delete variables in tuple, but you can do it list 
# s = {"Bob", "Rolf", "Anna"} #here you can not have two Bobs in set, but you can in typle and list. Also in set when you print for example 2 argument, you do not know what you get as it changes quite often

# l[0] = "Smith"
# l.append("Alex")
# l.remove("Alex")
# s.add("Ahmad")
# print(l)
# print(s)

#more about sets 
# friends = {"Bob", "Rolf", "Anna"}
# abroad = {"Bob", "Rolf"}

# local_friends = friends.difference(abroad)
# print(local_friends)

# local = {"Rolf"}
# abroad = {"Bob", "Anna"}

# total = local.union(abroad)
# print(total)

# art = {"Bob", "Jen", "Rolf", "Charlie"}
# science = {"Bob", "Adam", "Jen", "Anna"}

# both = art.intersection(science)
# print(both)

#Booleans
# local = {"Bob", "Anna"}
# abroad = {"Bob", "Anna"}

# print(local == abroad)

# local = ["Bob", "ANna"]
# abroad = ["Bob", "Anna"]

# lowercase_local = [name.lower() for name in local]
# lowercase_abroad = [name.lower() for name in abroad]

# print(lowercase_local == lowercase_abroad)

# movies_watched = ["The Matrix", "Green Book", "Her"]
# add_movie = input("Enter a movie you watched recently: ")

# if add_movie in movies_watched:
#     print(f"I have watched {add_movie} too")
# else:
#     print(f"I haven't watched {add_movie} yet")

# number = 7 

# user_input = input("Enter 'y' if you would like to play: ").lower()

# if user_input == "y":
#     user_number = int(input("Guess our number: "))
#     if user_number == number: 
#         print("You guessed correctly!")
#     elif number - user_number in (1, -1):
#         print("You were off bu one.")
#     else:
#         print("Sorry, it's wrong!")
#########################################################################
# List Comprehension
# numbers = [1, 3, 5]
# doubled = [x * 2 for x in numbers] 
# # OR 
# # for num in numbers:
# #     doubled.append(num * 2)

# print(doubled)

# friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# start_s = [ item for item in friends if item.startswith('S')]  # for item in friends if item.startwith('S') print item 

# print(start_s)
#########################################################################
# Dictionaries
# friend_ages = {"Rolf": 24, "Adam": 30, "Anna": 27} 
# print(friend_ages["Rolf"])
# print(friend_ages)

# friends = [
#     {"name": "Rolf", "age": 24},
#     {"name": "Adam", "age": 30},
#     {"name": "Anna", "age": 27},
# ]
# print(friends[1]["name"])

# student_attendance = {"Rolf": 96, "Bob": 80, "Anna": 100}

# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")

# # OR 

# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")

# user_input = input("Write a name of student: ")
# if user_input in student_attendance:
#     print(f"{user_input}: {student_attendance[user_input]}")
# else:
#     print(f"{user_input} is not a student in this class")

# attendance_values = student_attendance.values()

# print(sum(attendance_values) / len(attendance_values))

# x, y = 5, 11
# print(x, y)

# student_attendance = {"Rolf": 96, "Bob": 80, "Anna": 100}

# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")
##############################################################################################################################
# Functions in Python

# def hello():
#     print("Hello!")

# hello()

# def user_age_in_seconds():
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age is seconds is {age_seconds} seconds.")

# def user_age_in_minutes():
#     age_seconds = user_age * 365 * 24 * 60 
#     print(f"Your age is seconds is {age_seconds} minutes.")

# while True: 
#     user_age = int(input("Enter your age: "))
#     choise_value = input("Value to convert - mon, day, min, sec?: ")
#     if choise_value == "min":
#         user_age_in_minutes()
#     elif choise_value == "sec":
#         user_age_in_seconds()
#     else:
#         print("Goodbye")
#         break

# def add(x, y):
#     result = x + y 
#     print(result)

# add(5, 3)

# def say_hello(name, surname):
#     print(f"Hello, {name} {surname}")

# say_hello("Bob", "Smith")

# def divide(dividend, divisor):
#     if divisor != 0: 
#         print(dividend / divisor)
#     else:
#         print("You fucking BadAss!! I told you not to write fucking Zero!")

# user_dividend = int(input("Write a dividend: "))
# user_divisor = int(input("Write a divisor, but not 0: "))

# divide(user_dividend, user_divisor)
# RETURN VALUES IN FUNCTIONS  

# def my_function(x, y):
#     return x * y  # return means that this function returns value to the function that called it, not just displays it 

# my_function(10, 100) 

##############################################################################################################################################3
# Lambda function

# def add(x, y):
#     return x + y 

# print(add(5 ,7))   # OR rewrite this function as lambda

# print((lambda x, y: x + y)(5, 7))

# def double(x):
#     return x * 2 

# sequence = [1, 3, 6, 90]
# doubled = [double(x) for x in sequence]
# # OR 
# doubled = [(lambda x: x * 2)(x) for x in sequence] # lambda function
# print(doubled)

# Dictionary Comprehensions 

# users = [
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "longp4assword"),
#     (3, "username", "1234"),
# ]

# username_mapping = {user[1]: user for user in users}
# print(username_mapping)

student = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)}

def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades) 

def average_grade_all_student(student_list):
    total = 0
    count = 0
    for student in student.list:
        total = total + sum(student['grades'])
    return total / count 



