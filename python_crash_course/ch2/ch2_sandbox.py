name = 'donnie darko'

print('Lower case name: ' + name)

# Title method used here to capitalize first letters of words
print('Title case name: ' + name.title())

# Other methods that modify case of strings: lower & upper

print(name.upper())

#* It's often useful to use the lower method to store data entered by users, so all data is standardized to lower case. 
#* e.g. email addresses or usernames to prevent authentication issues if it's case sensitive

name='DONNIE dArKo'
print(name.lower())

firstname='donnie'
lastname='darko'

#! Concatenation

fullname = firstname + ' ' + lastname

print('My full name is ' + fullname.title())

#? Use what you've learned about concatenation and variables to create a message & print it to the console

message = 'Hello, ' + fullname.title() + '!'
print(message)

#! Adding whitespace to strings with tabs/newlines

# Add tab to string
print('\tString')

# New line + tab usage
print('String\n\tMore strings')

#! Stripping whitespace from a string

rightSpacedString = 'spacey '
leftSpacedString = ' spacey'
fullSpacedString = ' spacey '

# Temporarily strip whitespace from the left side
print(leftSpacedString.lstrip())

# Temporarily strip whitespace from the left side
print(rightSpacedString.rstrip())

# Temporarily remove whitespace from both right & left sides
print(fullSpacedString.strip())

# Strip method doesn't work on this one because the whitespace is in the middle, not the right or left sides
print(fullname.strip())


#! Escape apostrophe characters using a backslash
print('Apostrophe test, it\'s cool!')

#! Python uses two asterisks ** to calculate exponents

# 3 ** 2 = 9

age = 27
#print("I am " + age + " years old!")

#* Avoid errors generated from above code by using str() function:

print("I am " + str(age) + " years old!")