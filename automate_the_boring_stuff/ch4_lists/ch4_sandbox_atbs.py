# Chapter 4 - Lists

#* List value = list itself
#* Items in list separated by commas
#* Lists begin and end with square brackets

names = ['Bob', 'Devan', 'Sean', 'Spencer']

#! Nesting lists inside of lists can be done by simply adding another pair of square brackets as one of the values

stuff = ['baseball', 'basketball', ['cat','dog']]

#! Access the stuff in the nested list by using two indexes:

print(stuff[2][0]) #? Prints cat

#* Negative indexes count backwards in the list. [-2] = second to last, etc

#* Slices can be used to grab a selection of a list, forming its own list

#! The below code does not print "Sean", even though it includes index 2
print (names[0:2]) #? Slices take 2 indexes separated by a colon to grab all values up to, but not including, the last index. 

#* Ommitting an index on either side of the colon is the same as saying 'everything on this side'

print(names[:2]) #? Prints the same as the above

print(names[2:]) #? Prints 'Sean' and onward

#* Get the length of a list

print('Length of "names" list: ' + str(len(names)))

print(names.__len__()) #? Random weird way to get it, not shown in book - just randomly found it myself. Not sure what underscores mean

print(23.85 + 22.07 + 5.83)