def get_number():
    ''' tries to get a number from a silly user! '''
    # this is knows as a docstring and can be part of your code documentation
    num = input("Give me a number! ")
    while not num.isdecimal():
        print("That's not a number, try again!")
        num = input("Give me a number! ")
    # turning the correct input into  an integer before it is returned from the function
    return int(num)


# the main trick
# if this file is run -> then __name__ == "__main__"
# if this file is imported as a module -> the condition is not met
if __name__=="__main__":
    num1 = get_number()
    print("printing in module" + str(num1))