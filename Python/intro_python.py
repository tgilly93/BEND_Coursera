name = str(input('What is your name? '))
print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")
age = int(input('What is your age? '))
print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")
height = float(input('What is your height in meters? '))
print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")
loyalty = bool(input('Are you part of our loyalty program? '))
print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")
# Type casting with "input() method". Output will always be string. change to appropriate data type.

#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74
coffee = float(input('1 coffee @: $ '))
sandwich = float(input('1 sandwich @: $ '))
cake = float(input('1 cake @: $ '))
bill_total = coffee + sandwich + cake
print('Your total bill is $', bill_total)
#More type casting and user input() method.
  