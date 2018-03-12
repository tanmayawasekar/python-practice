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

name = "Tanmay"
age = 10.212    

print("My name is   %s and age is %d") % (name, age)
