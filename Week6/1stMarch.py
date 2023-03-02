# def get_user_input():
#     user_in = input("Give me a number! ")
#     return user_in

# discussion about naming convention
# use verb in function names to describe the action
#user_input = get_user_input()

# def do_sum(a, b, c):
#     return a + b + c
#
#
# simple tuple manipulation
# my_tuple = (4, 5, 6)
# # unpacking
# num1, num2, num3 = my_tuple
#
# print(do_sum(2, 3, 4))
# print(do_sum(num1, num2, num3))
# if we use the star notation when we pass in arguments into a function -> unpacking a tuple
# print(do_sum(*my_tuple))
#
#
# # variadic function - variable number of parameters
# def do_printing(name, *stuff):
#     print('Hello '+ name)
#     print(name, stuff, "cheese")
#
# the first argument will be 'name' all the rest will be packed into a tuple called 'stuff'
# do_printing("Martina", "Hello", "there", "chocolate", "milk")


def keep_count(user, comp, status):
    if status == 'user':
        user += 1
    else:
        comp += 1
    # returning multiple values from a function -> use a collection
    # here we return a tuple - no need for the parentheses
    return user, comp


# running_total_u =1
# running_total_c = 1
# first capture the returned value into a tuple
# result_tuple =keep_count(running_total_u ,running_total_c, 'user')
# unpack the tuple
# running_total_u, running_total_c = result_tuple
# print(running_total_u)
# print(running_total_c)
#
# do the previous steps in one
# running_total_u, running_total_c =keep_count(running_total_u ,running_total_c, 'comp')
# print(running_total_u)
# print(running_total_c)


def my_func(a):
    # a = 5
    print(a)

# defining a variable as global will allow the function to reach out of its scope and modify the variable called 'a'
def my_func2(b):
    global a
    a = 5

def my_fun3(f, num):
    # invoking the function
    f(num)

def triple(a):
    print(a*3)

def double(a):
    print(a*2)
# a = 6
# my_func2(a)
# print(a)

# passing function into function => function my_func3 is also known as a higher-order function
my_fun3(my_func, 7)
my_fun3(triple, 3)
my_fun3(double, 8)

# lambda function = anonymous function, function without a name
my_fun3(lambda a : print(a), 8)

# we can assign a lambda function to a variable so that we are able to call it
my_anon_func = lambda a: print(a*4)
# equivalent of the line above
# def my_anon_func(a):
#    print(a*4)
#my_anon_func = print(a*4)
my_anon_func(43)


# different types of import:
# import wed -> if we want to use a function from wed we need to use the full name: wed.get_number
# from wed import get_number -> now the get_number function can be called without the wed prefix
# import all available functions from module wed, no need to use prefix
from wed import *
num = get_number()