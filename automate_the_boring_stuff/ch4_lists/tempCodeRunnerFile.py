
onesy = ('one',) #? Having a comma at the end of a list or tuple is valid python code
                 #? If you try to put one value in a tuple without a comma, python will just think you're putting a value in parentheses for no reason

#* Check the variable type using the type() method

print(type(onesy)) #? <class 'tuple'>

onesy = ('poop','two') #? This is not the same as modifying the tuple. You're simply taking the values out of the var, then putting some other ones in.
print(onesy)

#onesy[0] = 'fart' #! Throws an error. Can't assign items
#print(onesy[0])

print(list(onesy[0])) #? Unexpected result: ['p', 'o', 'o', 'p'] - it turned the word poop into a list, with each character a separate item

print(list('testing'))

#* Convert tuple to list & try to reassign

(list(onesy))[0] = 'stope'

print(list(onesy[0]))