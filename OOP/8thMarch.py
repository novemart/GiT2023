# open file; different modes - open for reading, writing or appending
# f = open('myFile','r')
# reading the first ten characters
# line = f.read(10)
# reading the whole content of the file into one string
# also called slurping
#content = f.read()
# splitlines() method will split the string into lines and put them into a list
#lines1 = content.splitlines()
# similar to the above, the only difference is that it keeps the \n characters
#lines2 = f.readlines()
#print(lines1)
#print(lines2)

# best way to read from a file, specially if file very big
# for line in f:
#     print(line, end="")
#
# opening a file to write into it, if there was any content it will be erased
# f = open('myFile','w')
# writing individual strings
# #f.write("this is coming from Python!!")
# writing a list of stings into the file
# my_list=['apples\n', 'bananas\n', 'oranges\n']
# f.writelines(my_list)

from cat import Cat
from dog import Dog

# instantiating a class
# creating an instance = object
# need to pass in two parameters - declared in the constructor
catObj = Cat("Agnes", "grey")
catObj2 = Cat("Bentley", "black and white" )
animals = []
animals.append(catObj)
animals.append(catObj2)
# invoking methods
catObj.purr()
# invoking another method, passing a parameter
catObj.hunt("mouse")
catObj.hunt("birdie")
# _name is private and therefore should not be accessed directly
#catObj._name = "Tom"
print(catObj.get_name())
# should we set the values through setters or through the constructor?
# depends on if we know the value while we're creating the obj
catObj.set_height(40)
catObj2.set_height(45)
print(catObj.make_sound())
catObj.sleep()
catObj2.hunt("birds")
print(catObj2.get_name())
print(Cat.number_of_cats)

# strings are objects as well, they have a lot of methods we can use
# my_str = "Martina"
# my_str.

# creating an object of type Dog
dogObj = Dog("Fletcher", "black and brown")
dogObj.bark()
print(dogObj.make_sound())
dogObj.sleep()
print(dogObj)


# we can combine OOP and the functional approach
def printHello():
    print("Hello")

printHello()