# using functions

# def function():
# 	pass
# 	pass
# 	pass
# 	pass


# convention
# every function must have a name
# the function name must also follow the variable naming convention

# print(max([1,2,3,4,5,6,7,]))

# terms: function name, argument, return type
# example: a funtion to find the productr of two numbers

# function definition/declaration
def find_product(x_name, y_name):
	result = x_name * y_name
	print(result)

# function call
# print('Done')
# find_product(2, 4)


# the area of a circle of radius r = pi x r x r
# def find_Area(radius):
# 	area = 3.142 * radius * radius
# 	print(f'The area of circle of radius {radius} is {area}cm')

# find_Area(20)
# find_Area(40)
# find_Area(90)
# find_Area(102.5)

# area = 3.142 * 20 * 20
# print(f'The area of circle of radius 20 is {area}cm')

# area = 3.142 * 40 * 40
# print(f'The area of circle of radius 40 is {area}cm')

# area = 3.142 * 90 * 90
# print(f'The area of circle of radius 90 is {area}cm')

# area = 3.142 * 102.5 * 102.5
# print(f'The area of circle of radius 102.5 is {area}cm')



def getName():
	""" The purpose of the function """
	name = input('Welcome new user. \nPlease eneter your name: ')
	print(f'You have done well {name}.\
	This course will introduce you to core of Python programming.')

getName()
getName()