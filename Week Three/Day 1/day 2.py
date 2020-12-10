
# Striping a sting
# s = '    The String     '

# striped = s.strip()
# print(striped)


# Spliting strings
# s = '    The String     '
# striped = s.strip()	#strip the string
# splited = striped.split()
# print(splited)


# center a String
# print('  This is a centered string    '.center(100))

# Real word Example
# s = input('Enter your full name, first middlename lastname: ')
# s = s.strip()
# s = s.split()
# print(s)


# print('I am eating ' * 5)
# print('This is a line')
# print('This is another line')

# escape sequences
# \n   make a new line
# print('This is a line\nThis is another line')

# tab escape sequence
# \t 

# example: write a poem
# print('Title: Little Girl'.center(50))
# print('Little Little Little girl'.center(50))
# print('How I wonder what you are'.center(50))
# print('Like a diamond in the pool'.center(50))
# print()
# print('Title: Little Girl'.center(50))
# print('Little Little Little girl'.center(50))
# print('How I wonder what you are'.center(50))
# print('Like a diamond in the pool'.center(50))

# to comment/uncomment your python code in sublime text
# use control + /


# List
# create an empty list
# use list() or []

# example_list = []
# another_list = list()
shopping = ['shoes', 'clothes', 2, False, True]
# print(shopping[1])
list_with_sublist = ['shoes', 3, 5, [2, 3, 5]]

# indexing list
# start from zero: 0
# print(shopping[1])

s = 'a string'
# s[0] = 'b'
# print(s)
# lists are mutable: its contents can be changed
shopping[0] = 'bags'
# print(shopping)



# Tuple
# to create an empty tuple
# use tuple() or ()

my_tuple = tuple(('students', 'chairs', 'board'))
# print(my_tuple)


# List Indexing
# pets = list(('goldfish', 'cat', 'dog'))
# check = 'chicken' not in pets
# print(check)

# List Operators 
# # using + concatenation operator
# person1_pets = ['dog', 'chicken', 'goat']
# person2_pets = ['goldfish', 'duck', 'rabbit']
# joined = person1_pets + person2_pets
# print(joined)


# using * multiplication operator (used to make copies of a list)
person1_pets = ['dog', 'chicken', 'goat']
joined = 2 * person1_pets

# to get the lenght of the list
# use len() function
# result = len(joined)

# # to get the smallest item in the list
# # use min() function
# lst = [2, 4, 6, 8]
# result = min(lst)
# print(result)


# to get the largest item in the list
# use max(lst) function
# lst = [2, 4, 6, 8]
# result = max(lst)
# print(result)


# to get the sum of items in the list
# use sum() function
# lst = [2, 4, 6, 8,]
# result = sum(lst)
# print(result)



# List Methods
# add an item to a list
# use append(value) function
# lst = [2, 4, 6, 8]
# lst.append(200)
# print(lst)

# find the number of occurences of item in a list
# use count(value) function
# lst = [2, 4, 6, 8]
# lst.append(2)
# result = lst.count(2)
# print(result)
# print(lst)



# find the index (location) of an item in a list
# use index(value) method
# lst = [2, 4, 6, 8]
# result = lst.index(2)
# print(result)
# print(lst)


# add an item to a list at a defined location
# use insert(index, value) function
# lst = [2, 4, 6, 8]
# lst.insert(3, 200)
# print(lst)


# get the last item in a list
# use pop() method
# lst = [2, 4, 6, 8]
# lst.pop()
# result = lst.pop()
# print(result)
# print(lst)


# remove the first occurence of an item in a list
# use remove(value) method
# lst = [2, 4, 6, 8]
# lst.remove(8)
# print(lst)


# reverse the order of items in a list
# use reverse() function
# lst = [2, 4, 6, 8]
# lst.reverse()
# print(lst)



# sort a list: arrange list in ascending order
# use sort() function
# lst = [10, 5, 7, 2, 4, 6, 8]
# lst.sort()
# print(lst)

# use sorted() function
# lst = [10, 5, 7, 2, 4, 6, 8]
# result = sorted(lst)
# print(result)




# Slicing Lists
colors = ['red', 'yellow', 'indigo', 'white', 'green']
# print(colors[0])
# ['red']
# result = [colors[0]] + colors[2: 5]
# print(result)
colors.remove('yellow')
print(colors)
