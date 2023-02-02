# import math
# myNum = math.cos(15)

# * is a wildcard = everything
# no need to use the prefix math.
from math import *
# myNum = cos(15)

# g = 9.81
# v_0 = 44
# deg = 80
# theta = deg * (pi / 180)
# x = 0.5
# y_0 = 1
#
# numerator = g*x*x
# denominator = 2*(v_0*cos(theta))**2
#
# mini_result = numerator/denominator
#
# print(y_0 + x*tan(theta) - mini_result)

# my_input = input("type in number 1: ")
# my_input2 = input("type in number 2: ")
# # changing the type on my_input from string to an int
# print(my_input.isdecimal())
# my_num1 = int(my_input)
# # changing type of my_input2 from string to a float
# my_num2 = float(my_input2)
#
# print(my_num1 + my_num2)

# list - mutable ordered collection, positions start at 0
# my_list = [1, 2, 3, 4]
# print(my_list)
#
# print(my_list[2])
# my_list[2] = -4
#
# my_list.append(9)
# print(my_list)
#
# my_second_list = [1, 'Martina', [2, 4, 5]]
# print(type(my_second_list))
# print(my_second_list[2][1])
# print(len(my_second_list))

# tuple - immutable ordered collection, positions start at 0
# my_tuple = (1, 2, 3)
# print(type(my_tuple))
# print(my_tuple[1])

# IMMUTABLE
#my_tuple[1] = -9
#my_tuple.append(9)

# set - mutable, unordered; UNIQUE elements
# my_set = {1, 2, 3}
# print(type(my_set))
# my_set.add(7)
# print(my_set)
# my_set.add(1)
# print(my_set)
# # UNORDERED
# # my_set[1]
#
# # dictionaries - key value pairs, unordered
# my_dict = {'first_name': 'Martina', 3: [1, 2, 3, 4], 'address': 'Brighton'}
# print(my_dict['first_name'])
# print(my_dict[3][2])

# my_num = 0
# my_input = input("Gimme a number: ")
# if my_input.isdecimal():
#     my_num = float(my_input)
#     if my_num > 5:
#         print("You gave me a number greater than five!")
#         print("Special line of code")
#     else:
#         print("number is not greater than five!")
# else:
#     print("That's not a number!")

# light = "blue"
#
# # check for equality
# if light == 'red':
#     print("STOP!!!")
# elif light == 'amber':
#     print("Watch out!!")
# elif light == 'green':
#     print("go!")

#user_input = input("Type something ")
# ! logical NOT
# if user_input != '':
#     print(user_input.upper())
# else:
#     print("You have not typed anything!")


# if user_input:
#     print(user_input.upper())
# else:
#     print("You have not typed anything!")

# my_list = ['chocolate', 'tea', 'scones']
# if 'CHOcolaTE'.lower() in my_list:
#     print("we are good")
# else:
#     print("Put chocolate on the list immediately!")

# bus = 100
# if bus == 67 or bus == 100:
#     print("I am getting on")
# else:
#     print("I'm not getting on")

#i = 0
# while i < 7:
#     print(i)
#     i += 1

# my_input = input("Type a number")
# while not my_input.isdecimal():
#     my_input = input("Type a number")


my_list = ['chocolate', 'tea', 'scones']
# # for every element in my_list do ....
for element in my_list:
    print(element)

for pos, e in enumerate(my_list):
    print(e + " is on position " + str(pos))

# position = 0
# while position < len(my_list):
#     print(my_list[position])
#     position += 1

# i = 0
# while i < 5:
#     print("hello")
#     i += 1

# for i in [1, 2, 3, 4, 5]
# for i in range(1, 6):
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue
#     print("hello")






