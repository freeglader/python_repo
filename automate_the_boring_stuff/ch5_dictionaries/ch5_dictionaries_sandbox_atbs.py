# Chapter 5 - Dictionaries and Structuring Data

#* Dictionaries are created with curly braces

myFaves = {'food': 'orange chicken', 'drink': 'diet coke', 'artist': 'travis scott', 'book': {'title': 'Pimp: The Story of My Life', 'author': 'Iceberg Slim'}} 

print(myFaves)

#? Playing with nested dictionaries
print('My favorite book is: ' + myFaves['book']['title'] + '. The author is known as ' + myFaves['book']['author'] + '.')

for value in myFaves.values():
    print(value)

for item in myFaves.items():
    print()

print('---------------------- TESTING ----------------------\n')
# The following line will return a list object 
print(list(myFaves.keys()))

#?  You can use a for loop to put the key & value in to two separate variables to work with. Cool.

for k, v in myFaves.items():
    # Prints out the key & value for each of the items. Could also use these keys/values in other useful ways in actual programs.
    print('Key: ' + str(k) + ' | Value: ' + str(v))

#? Check if a key / value is in a dictionary with the same methods

if 'diet coke' in myFaves.values():
    print('Hell yeah!!')
else:
    print('Hell nah!!!')

#? Use get() method to specify a key plus a fallback value to return if the key doesn't exist.

print('My favorite drink is ' + myFaves.get('drink', 'Dr. Pepper')) #! The fact that I had a key called drink made the program list "diet coke", but if I were to delete it, the value would be "Dr. Pepper" as specified  here.

#? setdefault() method: 1st arg = key to check for, 2nd arg = value to set for that key if it doesn't exist

spam = {'name': 'Dan', 'age': 45 }

spam.setdefault('color', 'white') #! This automatically creates a key called 'color' and a value 'white' because it didn't exist
spam.setdefault('color', 'black') #! This doesn't change anything, because the dict already contained the key 'color'

#* setdefault() method mini program - count all the occurences of the characters in the following message:

message = 'Underneath the bridge the tarp has sprung a leak'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1
print('MESSAGE: ' + message + '\n')
print('Number of occurences for each character: \n')
print(count.items())
