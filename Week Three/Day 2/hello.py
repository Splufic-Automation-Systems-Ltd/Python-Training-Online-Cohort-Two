
# lst = list([12, 30, 10, 4, 100])
# maximum = max(lst)
# print(f'The maximum age of students in the class is {maximum}')

# name = input('Enter your first name: ')
# print(f'Your first name is {name}')


# math module is named math.py
# to use the mofule ww need to import it
# import math

# using sqrt(x)
# x = 9
# result = math.sqrt(x)
# result = int(result)
# print(f'The square root of {x} is {result}')

# using ceil(x)
# x = 9
# result = math.ceil(x)
# # result = int(result)
# print(f'The ceil of {x} is {result}')

# print(f'The constant pi is {math.pi}')



# # Single selection condition
# temp = eval(input('Enter the current temperature: '))
# if temp >= 86:
# 	print('It is hot!')
# 	print('Be sure to drink liquids.')


# # double selection condition
# temp = eval(input('Enter the current temperature: '))
# if temp > 86:
# 	print('It is hot!')
# 	print('Be sure to drink liquids.')
# else:
# 	print('It is not hot!')
# 	print('Bring a jacket!')
# print('Goodbye!')



# multiple selection condition
# score = eval(input('Enter the student\'s score: '))
# if score <= 39:
# 	print('You failed')
# elif score >= 40 and score < 50:
# 	print('You passed averagely.')
# elif score >= 50 and score < 60:
# 	print('You passed a little above average.')
# elif score >= 60 and score < 70:
# 	print('You passed a little below exelent.')
# elif score > 70:
# 	print('You passed excelently')
# print('Goodbye!')


# iterable contains several items
# e.g list, strings, tuple, set

# create an iterable
# # make a list of students in the class
# studentlist = ['Tolu', 'Paul', 'Jide', 'Hammed']
# studentlist = studentlist * 10
# print(studentlist) 
# # print(studentlist[0])
# # print(studentlist[1])
# # print(studentlist[2])
# # print(studentlist[3])
# # print(studentlist[4])
# print('printing the names of studenst in the list: ')
# for name in studentlist:
# 	print(name.upper())



# class work
# # get the year fromn the user 
# year = eval(input('Enter the year: '))
# # if it is a leap year, print 'could be a leap year'
# if (year % 4) == 0:
# 	print('Could be a leap year')
# # else, print 'defintaely not a leap year'
# else:
# 	print ('defintaely not a leap year')