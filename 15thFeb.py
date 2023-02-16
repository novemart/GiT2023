# my_list = ['1', '4', '6', '10']
# demonstration of the map function - accepts a function and applies it to every element of the supplied list
# the result is then turned into a list type
# new_list = list(map(int, my_list))
#
# alternative way of achieving the same thing as above
# result = []
# for num in my_list:
#     result.append(int(num))
#
# another example application of the map function - create a list with the number of characters in each word
# my_other_list = ['milk', 'bread', 'lipstick']
# my_len_list = list(map(len, my_other_list))
# print(my_len_list)

# are string more like tuples or lists?
# strings are immutable and therefor more similar to tuples
# my_dirty_str = "Martina"
# # my_str[4] = "x"
# we are creating a new string
# my_sanitized_str = my_dirty_str.replace('i', 'x')
# print(my_dirty_str)

# few handy functions that work on number collections - max, min, sum
# len -> returns the number of elements
# may lead to errors or unexpected results if the list does not contain only numbers
# my_num_list = [3, 6, "martina", 2, 3]
# max, min, len
# print(max(my_num_list))
# print(sum(my_num_list))
# my_num_list.append(6)

# TUPLES
# my_tuple = (5, 7, 2)
# the parentheses are optional when creating a tuple
# # my_tuple = 5, 7, 2
# print(my_tuple)
# if we want to create a tuple with only one element in it
# # trailing comma
# my_tuple_one = (5,)
# my_tuple_one2 = 5,
# print(type(my_tuple_one))
#
# # unpacking a tuple
# if the number of variables on the left-hand side does not match the number of elements in the tuple => error
# a, b, c = my_tuple
# print(a, b, c)
#
# combining the above principles - creating tuple without the parentheses and unpacking it into three variables
# looks like we are able to create and assign values to multiple variables in one line
# a, b, c = 5, 7, 2
#
# # swapping value
# d = 6
# e = 9

# normally, we would need a third variable - think of two glasses that you want to swap the contents of
# f = d
# d = e
# e = f
#
# # very Python specific!!
# again, leveraging the notion of creating tuple without parentheses
# right-hand side is ALWAYS evaluated first
# d, e = e, d


#LISTS
my_list = ['milk', 'bread', 'chocolate', 'cheese', 'onions']
# indexing from the right-hand side uses negative numbers
# print(my_list[-1])
# # slicing
# print(my_list[2:4:2])

# coming back to unpacking a list ('unpacking with a wildcard'), notice the star before the variable b
# first element will be placed into variable a, last element into variable c and everything else
# will be assigned to variable b - notice the different type
# a, *b, c = my_list
# print(type(a))
# print(type(b))
# print(c)
#
# prepending element to a list - adding at the beginning
# my_list[:0] = ['shoes', 'tea']
# print(my_list)
# # same thing as append, works only for multiple elements in a list
# my_list += ['dog food', 'sea food']
# print(my_list)
#
# insert element at a specific position
# my_list.insert(-3, 'rice')
# print(my_list)
#
# # last element removed and returned
# last_elem = my_list.pop()
# print(my_list)
# print(last_elem)
#
# remove element at a specific position
# my_list.pop(5)
# print(my_list)

# SETS - no notion of position, only unique elements
my_set = {4, 7, 2, 4, 7, 2, 5, 6, 8}
# alternative way to create a set or list - built-in functions set() and list()
# my_set2 = set()
# my_list2 = list()
print(my_set)

# removing an element from a set
num = my_set.pop()
print(num)
print(my_set)

# discard will remove the given value
my_set.discard(11)
print(my_set)

# adding elements to a set
my_set.add(-4)
print(my_set)
my_set.add(11)
print(my_set)

# creating a set out of a string - demonstrating the ability to turn one collection into another type
# very useful for going from list to a set which will remove automatically all duplicate elements
name = 'Martina'
my_new_set = set(name)
# notice only one 'a', and the order of characters is not persisted
print(my_new_set)

# DICTIONARIES ; key: value pairs, no notion of positions, keys need to be unique
my_dict = {'key1': 'value1', 'key2': 'value2'}
# access elements using their key
print(my_dict['key1'])
# adds a new element into the dictionary
my_dict['key3'] = 'value3'
print(my_dict)
# removes element with a specific key; error if the key is not present
# my_dict.pop('key4')

