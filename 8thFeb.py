# demonstration of incorrect usage of the break statement, the only way how we can
# escape from an infinite loop, prone to errors
# attempts = 0
# while True:
#     if attempts == 1:
#         break
#     attempts += 1
#
# correct usage of the break statement, we have a finite loop, in this case loop that will run 3 times at most
# however, in a situation when we find the correct pin on first or second attempt, we want to exit the loop sooner
# supplied_pin = ''
# while attempts < 3:
#     if supplied_pin == '1234':
#         print("You got it!")
#         break
#     attempts += 1

# range function is used to create a collection of integers ranging from the 'start' number until 'stop-1'
# the default step size is one, and doesn't have to be specified
# range(start, stop, stepSize*) => start, start+stepSize, start+stepSize, start+stepSize, ... ,stop-1
# for i in range(0, 3):
#     if supplied_pin == '1234':
#         print("You got it!")
#         break
#
# for i in range(0, 5, 2):
#     print(i)

# naming convention - variable names start with lower case

# your loop can have an else part - this part is only executed if the loop is exhausted = stopped naturally
# for i in range(0, 3):
#     if i == 2:
#         break
#     print(i)
# else:
#     # only run when the loop is exhausted, it stops naturally
#     print("Im done!")

# an example of defensive coding - asking the user for a number until the input contains only numbers
# num = input("Type in a number: ")
# while not num.isdecimal():
#     print("That's not a number!!")
#     num = input("Type in a number: ")
# else:
#     num_int = int(num)

# this is potentially dangerous as the user may have typed something that doesn't contain only numbers
# therefore can not be safely turned into an int
# num = int(input("Type in a number: "))

# ask the user for two numbers and print the bigger one
# a = int(input("Type in first number "))
# b = int(input("Type in second number"))
# max_num =0
# if a > b:
#     max_num = a
# else:
#     max_num = b
#
# # conditional expression, only works for the full if-else statement
# expression = returns a value; statement = doens't return a value
# max_num = a if a > b else b
#
# print(max_num)

# infinite loop, to stop it press the red square button and observe the exit code in the terminal
# while True:
#     print("hello")

# examples of emojis
# print("\U0001F600")
# print("\U0001F649")
# print("\N{winking face}")

# open up the terminal tab at the bottom and typed in
# pip install emoji
# import emoji
# print(emoji.emojize("Hello from :robot:"))


# experimenting with the print function - the optional parameters sep and end
# sep - separator, character written between the individual elements - by default empty space
# end - last character included in the print - by default new line character  \n
# a = "World"
# b = "Hello"
# print(b, a, "from Martina")
# print(b, a, "from Martina", sep='*')
# print(b, a, "from Martina", end="!!!!")
# print("Hello?")
#
# example usage of sep property, numbers written in one line
# for i in range(0, 10):
#     print(i, end=' ')
# print()

# option for formatting output, print function takes variable number of parameters
# print(5, "+", 3, '=', 8)
#
# # strings can be denoted with single or double quotes
# myStr = 'Martina'
# myStr2 = "Martina"
#
# the only difference is when the actual literal value needs to contain a ' or "
# lastName = "O'Neill"
# lastName2 = 'O"Neill'
# lastName3 = 'O\'Neil'
#
# special characters for new line and tab(bigger empty space)
# longString = "fdafhd\nfndjkvhdg\tirshgjkfdbnfjk\nghdfjkghfj\nkgfnbkj"
# print(longString)

# raw string - none of the special characters is translated, value taken as is
# rawString = r"\U0001F649"
# rawString2 = r"fdafhd\nfndjkvhdg\tirshgjkfdbnfjk\nghdfjkghfj\nkgfnbkj"
# print(rawString2)

# concatenation
# name = 'Martina' + " " + 'Yusuf'
# print(name)
#
# access character on position 4
# print(name[4])
# strings are immutable - can not reassign individual characters
# name[4] = 'y'

# a = 5
# b = 6
# another example of formatting a simple combination of numbers and letters
# print(str(a) + " + " + str(b) + " = " + str(a+b))
#
# example of replace method - finds a substring and replaces it with new values
# always returns a new string
# myStr = "I like chocolate more than cheese."
# newStr = myStr.replace("cheese", "wine")
# print(newStr)
# print(myStr)

# myList = ["wine", "cheese", "biscuits", "cat food"]
# myStr = ""
# #  very resource intensive!! always creates a new string because strings are immutable!
# for el in myList:
#     myStr += el
# print(myStr)

# if the substring is not found , value -1 is returned
# print(myStr.find("cheeses"))
#
# title case
# print(myStr.title())
#
# a = 5
# b = 3
# use f-strings to interpolate variables - replaces the name of variable by its value
# result = f"{a} + {b} = {a+b}"
# result2 = "{} + {} = {}".format(a, b, a+b)
# print(result)
# print(result2)

# string slicing - creating a substring starting at 'start' position and stopping at 'stop-1' position
myStr = "I like chocolate more than cheese."
# [start: end] - end non-inclusive
print(myStr[2:9])
# doesn't return anything, start position is after stop position
# print(myStr[9:2])

# we can also use the negative number positioning - counting from right starting at -1
print(myStr[-4: -1])
# ex. localhost:8080/hello/
# I want the whole string apart from the last character
my_url = "localhost:8080/hello/"
print(my_url[:len(my_url)-1])
print(my_url[0:-1])
# if start position not specified - starting at position 0
# if end position not specified - stopping at the end of the string
print(my_url[:-1])

print(my_url[5:])

# copy - omitting start and stop positions will return the whole string back and therefore create a copy
my_url_copy = my_url[:]
print(my_url[:])

# split method - create a list splitting the string where a certain character occurs - by default empty space
myStr = "I like chocolate more than cheese."
my_list = myStr.split()
print(my_list)

# optional parameter - where do we want to split the initial string?
my_list2 = my_url.split("/")
print(my_list2)

# the opposite functionality - creating a string out of a list of values
# concatenate the items together using a special delimiter
# the method is called on the delimiter!
myList = ["wine", "cheese", "biscuits", "cat food"]
my_list_string = ' '.join(myList)
print(my_list_string)
