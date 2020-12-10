# declare the list of users
lst = ['joe', 'sue', 'hani', 'sophie']


# # complexity: time and space

# O(n) O(40000)
# O(1)
# O(log(n))

# get user input
# login = input('Enter your id: ')
# login.lower()
# check if user exists in list

# method 1
# for item in lst:
# 	if item == login:
# 		print(f'Login: {login} \
# 				You are in! \
# 				Done.')
# 		break
# else:
# 	print(f'Login: {login} \nUser unknown. \nDone.')
# print the result

# method 2
# if login in lst:
# 	print(f'Login: {login} \nYou are in! \nDone.')
# else:
# 	print(f'Login: {login} \nUser unknown. \nDone.')


# method 3
# time complexity: O(1)
# count the occurence of login in lst
# if lst.count(login) == 1:
# 	print(f'Login: {login} \nYou are in! \nDone.')
# else:
# 	print(f'Login: {login} \nUser unknown. \nDone.')



# allow new users to sign up
# get the new user id 
user_id = input('Enter new user id: ')
# add it to the list
lst.append(user_id)
# print the list
print(f'A new user, {user_id} has just been added. ')