# # # values = [2, 3, 2, 4]

# # # def my_transformation1(num):
# # #     return num ** 2


# # # for i in map(my_transformation1, values):
# # #     print(i)

# # # values = [2, 3, 2, 4]

# # # def my_transformation2(num):
# # #     return num * 2

# # # for i in  map(my_transformation2, values):
# # #     print(i)
# # # #***_map will call the function for each value in the list.
# # # # The ** operator in the function raises the parameter to the power of 2._**

# # # p = ["L", 'u', 'a', 'i']
# # # print p

# # # p[0] = p[0].lower()
# # # print p

# # # my_string = "This is my String"
# # # print my_string
# # # for c in my_string:
# # #     print c.upper(),

# # # def say_hello():
# # #     return "hello"

# # name = "Luai Ahmed Muhammed Shrair Ghazali"

# # print( name)

# # # son1_name = "Abdurrahman"
# # # son2_name = "Ahmed"
# # # son1_fullname = '{} {}'.format(son1_name, name)
# # # print(son1_fullname)
# # # hello_son1 = 'Hello {}. Welcome to the Python programming world!'.format(son1_name)
# # # print (hello_son1)

# # # my_message = f'{name} welcomes his son {son1_name}' #This works in Python 3.6 or after

# # #print(dir(name))
# # #print(son1_name)
# # #print(help(str.find))
# # #print(name.swapcase())
# # names_list = ["Luai", "Hana", "Abdurrahman", "Jood",
# #             "Eithar", "Ahmed",]
# # #print(names_list)
# # #print(min(names_list))

# # fullname_list = name.split(' ')
# # print(fullname_list)

# # a = [1,2,3,4,5]
# # b = [1,2,3,4,5]
# # fish1 = "Dusky"
# # fish2 = "Dusky"
# # fish3 = "Amberjack"
# # fish4 = "Trigger Fish"

# # print a, b , a is b
# # print fish1, fish2, fish1 is fish2
# # print(id(a), id(b))
# # print (id(fish1), id(fish2))

# import turtle

# def new_window():
#     my_window = turtle.Screen()
#     my_window.bgcolor("beige")


# def draw_something():
#     picasso = turtle.Turtle()
#     picasso.shape("circle")
#     picasso.color("green")
#     picasso.speed(3)
    

# new_window()
# draw_something()
# print (help(turtle.Turtle))



'''
READING FROM FILE AND CHECKING FOR PROFANITY
'''
# import urllib

# my_file = open(r'd:\Documents\1map\test_file.txt')
# goodgood = "NO BAD WORDS DETECTED"
# badbad = "BAD WORDS DETECTED"
# for line in my_file:
#     connection = urllib.urlopen(r"http://www.wdylike.appspot.com/?q="+str(line))
#     is_bad = connection.read()
#     connection.close()
#     print line + "\n is_bad: " + str(is_bad)
    
#     if is_bad:
#         print badbad
#     else:
#          print goodgood
#     is_bad = False
    
# # my_file.seek(0)
# # line2 = my_file.readline()
# # print(line2)
# my_file.close()

import math
x1 = 2
x2 =5
y1=6
y2=2
print math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))