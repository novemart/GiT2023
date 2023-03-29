# try:
#     num = int("martina")
# except ValueError as e :
#     print(e)
#
# # print(num)
# try:
#     f = open("foo2")
#     print("Today is wednesday")
#     print("We saw Shona earlier")
# except FileNotFoundError as e:
#     print("File was not Found")
#     print(e)
# except Exception as e:
#     print("The value is invalid")
#
# else:
#     print("Ran when the exception does not happen!")
# finally:
#     print("It is run if the exception is triggered but also if it's not")


def buyADrink(age):
    if (age>18):
        #payForDrink()
        #print("OK")
        pass
    else:
        raise ValueError("Under Age")


buyADrink(16)