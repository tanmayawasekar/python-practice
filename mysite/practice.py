from timeit import timeit, time, repeat

# # my_name = "tanmay"
# # my_second_name = "nanu"
# # my_third_name = "tanu"

# # print("My name is %s , my second name is %r and third name is %s") % (my_name, (my_second_name,), my_third_name)

# # end1 = "C"
# # end2 = "h"
# # end3 = "e"
# # end4 = "e"
# # end5 = "s"
# # end6 = "e"
# # end7 = "B"
# # end8 = "u"
 
# # end9 = "r" 
# # end10 = "g"
# # end11 = "e"
# # end12 = "r"
# # # watch that comma at the end. try removing it to see what happens
# # print (end1 + end2 + end3 + end4 + end5 + end6)
# # print end7 + end8 + end9 + end10 + end11 + end12


# print("How old are you?")
# age = raw_input()
# print "How tall are you"
# height = raw_input()
# print "How much do you you weigh"
# weight = raw_input()

# print("SO ypu are %s year old, %d tall and %s heavy") % (age, int(height), weight) 

# from sys import argv

# first, script,  second, third,  = argv

# print(type(first))

# print "the first script is called:", script
# print "first variable:", first
# print "second variable:", second
# print "third variable:", third

# from sys import argv
# from os.path import exists

# script, from_file_name, to_file_name = argv

# if not exists(from_file_name):
#     raise "FileNoneFound"

# file1 = open(from_file_name, mode="r+")

# file1_text  = file1.read()

# file2 = open(to_file_name, 'r+')

# file2.write(file1_text)

# print(open_file_object)

# print(open_file_object.read())


# print "Truncating fille"

# open_file_object.truncate()

# print("after truncatting the file", open_file_object.read())

# # print("file pointer", open_file_object.seek())

# first_line = raw_input("Enter the first line:")
# second_line = raw_input("Enter the second line:")
# third_line = raw_input("Enter the third line:")
# open_file_object.write(first_line)
# open_file_object.write(second_line)
# open_file_object.write(third_line)

# raw_input("Please check the file is changed and not and press enter")

# print open_file_object.read()

# open_file_object.close()

# firstname = "tanmay"

# from urls import 


# def examplefunction(firstname):
#     global firstname
#     firstname = "awaselar"
#     print(firstname)
#     return firstname


# examplefunction(firstname)
# print(firstname)
# print(bool([]))
# if '':
#     print("tanmay")
# elif []:
#     print("askfaksf")
# elif "askfafk":
#     print("fmanfanf")

# for value in range(10, 0, -2):
    # print(value)

# name = "Tanmay"
# age = 10.212    

# print("My name is   %s and age is %d") % (name, age)
# def getSquare(x):
    # return x**2


# print("with range",repeat(stmt="'-'.join(str(n) for n in range(100))",
# setup="from practice import getSquare", number=100000, repeat=10))

# print("with xrange",repeat(stmt="'-'.join(str(n) for n in xrange(100))",
# setup="from practice import getSquare", number=100000, repeat=10))

####################################################################
# from functools import wraps

# def check_negetive(fn):

#     @wraps(fn)
#     def inner_function(*args, **xargs):
#         positive_list_posi = [True if x > 0 else False for x in args]
#         positive_list_named = [True if value > 0 else False for index,
#                                value in xargs.items()]

#         if len(positive_list_posi) and not all(positive_list_posi):
#             raise ValueError('Arguments must be non negetive')
        
#         if len(positive_list_named) and not all(positive_list_named):
#             raise ValueError('Arguments must be non negetive')
#         return fn(*args, **xargs)

#     return inner_function


# def print_in_out_params(fn):

#     @wraps(fn)
#     def inner_function(*args, **argsx):
#         print(args, argsx)
#         result = fn(*args, **argsx)
#         print(result)
#         return result
        
#     return inner_function    

# @check_negetive
# @print_in_out_params
# def square(x, y):
#     return x * 2 + y * 2

# square(x=2,y=3)

# print square.__name__


class example_static_methods(object):
    _initial_roll_no = 10

    @classmethod
    def get_next_roll(cls):
        cls._initial_roll_no += 1
        return cls._initial_roll_no


    def __init__(self):
        example_static_methods._initial_roll_no+=1
        self._initial_roll_no = self.get_next_roll()

    @property
    def roll_no(self):
        return self._initial_roll_no

    @roll_no.setter
    def roll_no(self, value):
        if value < 0:
            raise ValueError("Non Negetive values not allowed")
        self._initial_roll_no = value

a = example_static_methods()
example_static_methods.get_next_roll()

a.roll_no = -2
print(a.roll_no)
