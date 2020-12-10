


# find the lowest of 34.99, 29.95, 31.50
""" 
Algorithm:
	set lowest to 34.99
	if lowest is greater than 29.95, set lowest to 29.95
	else if lowest is greater than 31.50, set lowest to 31.50
	print lowest
"""

# lowest = 34.99
# if lowest > 29.95:
# 	lowest = 29.95
# if lowest > 31.50:
# 	lowest = 31.50
# print(lowest)



# Method 2:arg1, arg2
# use the min function to get the minimum value of 
# numbers in a list

result = min(34.99, 29.95, 31.50)
print(result)
