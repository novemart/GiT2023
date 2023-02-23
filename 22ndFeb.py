# my_set = {} it will create a dictionary, need to use the set() function
# my_set = set()
# my_list = []
# my_tuple = ()

# print(type(my_set))
#
# example of a dictionary with more complicated structure
# histDict = {
#     1 : {'operator' : '+', 'num list': [3,4,6,7,8], 'total': 28},
#     2 : {'operator' : '/', 'num list': [3,4,6,7,8], 'total': 0.00000342423}
# }
#
# accessing the operator of the second equation kept in the dictionary
# print(histDict[2]['operator'])
#
# creating a list of all operators used in the calculator; looping through the values
# operators = []
# for eq in histDict.values():
#     operators.append(eq['operator'])
#
# print(operators)
#
# example of looping through the items of the dictionary
# the key:value pairs are organised into tuples
# for it in histDict.items():
#     print(it)
#
# looping through the keys of the dictionary
# for k in histDict.keys():
#     print(k)

# FUNCTIONS
# function declaration
# it does not do anything, does not run this code unless we call the function
def print_hello():
    print("hello")


# function invocation, function call
# print_hello()
#
#
# defining a function with two parameters
# function does not return anything, prints the result into the terminal
def addition(num1, num2):
    # example of a local variable and the difference in scope
     localVar = 9
     print(num1+num2 +localVar)
#
# calling the function using literal numbers
# addition(4, 8)
# calling the function and passing expressions as the two parameters
# addition(4-7, 1+9)
#
# var1 = 19
# var2 = -4
# calling the addition function and passing values of two variables as parameters
# addition(var1, var2)

# testing the difference in scope
# # print(num1)
# # print(localVar)
#
# even though the variables are called the same as the parameters of the addition function
# these are different - different scope!
# num1 = 4
# num2 = 9
# addition(num1, num2)

# another function taking two parameters - now returning the result back to the caller
# def subtraction(num1, num2):
#     result2 = num1 -num2
#     print(result2)
#     #return num1 - num2
#     return result2
#
#
# make sure you are able to access the returned value, use a variable assignment
# result = subtraction(5, 9)
# print(result)
# directly print the returned value, we are not able to access it later on though
# print(subtraction(5, 3))


# example of error checking functionality for the calculator, does not need any additional information
# def get_number():
#     num = input("Give me a number! ")
#     while not num.isdecimal():
#         print("That's not a number, try again!")
#         num = input("Give me a number! ")
    # turning the correct input into  an integer before it is returned from the function
#     return int(num)
#
#
# essentially the calculator function, takes two number and an operator; returns the result
# def calculate(num1, num2, operator):
    # example of making a function call inside another function
#     print_hello()
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1-num2
#
#
# calculator
# first = get_number()
# second = get_number()
# result = calculate(num1 = first, num2 = second, '+')
# print(result)

# python passes parameters by assignment - as if by nickname
# def change(a):
#     a = 7
#
# def change2(a):
#     a += ['hello','there']
#     return a
#
# myVar = 8
# change(myVar)
# print(myVar)
#
# my_list=['Martina']
# my_returned_list = change2(my_list)
# print(my_list)
# print(my_returned_list)


# example of default parameter
def calculate_tax(price, tax=0.2):
    result = price * (1+tax)
    return result

book = 12
chocolate = 5
# example of passing arguments using their name rather than their position
print(calculate_tax(price=book))
# if function is called without supplying the tax value, the default value will be used
print(calculate_tax(chocolate))
gin = 20
# calling the function with both parameters - the defualt value will not be used
print(calculate_tax(gin, tax=0.3))

# enforcing naming parameters, every parameter declared after the * must be passed in using its name
# firstParam can be passed using its position
def calculate_tax2(firstParam, *,price, tax=0.2):
    result = price * (1+tax)
    return result

# if we don't use the price= or tax= we will get an error
print(calculate_tax2(7, price=book, tax=0.4))




