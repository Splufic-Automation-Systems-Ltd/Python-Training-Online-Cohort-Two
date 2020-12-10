
import math
# a python program that converts temperature from Farenheit to Celcius

# get the user input
fahrenheit = input('Enter the temperature in degrees Fahrenheit: ')
# calculate the result
result = (5/9 * (int(fahrenheit) - 32))
result = math.trunc(result)
# print the result
print(f'The temperature in degrees Celsius is {result}')