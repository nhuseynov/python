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

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
start_s = [ item for item in friends if item.startswith('S')]

print(start_s)
