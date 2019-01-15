# Chapter 4 - Lists

#* List value = list itself
#* Items in list separated by commas
#* Lists begin and end with square brackets

names = ['Bob', 'Devan', 'Sean', 'Spencer']

#: Nesting lists inside of lists can be done by simply adding another pair of square brackets as one of the values

stuff = ['baseball', 'basketball', ['cat','dog']]

#TODO: Access the stuff in the nested list by using two indexes:

print(stuff[2][0]) #? Prints cat

#! Negative indexes count backwards in the list. [-2] = second to last, etc

#! Slices can be used to grab a selection of a list, forming its own list

#TODO: The below code does not print "Sean", even though it includes index 2
print (names[0:2]) #? Slices take 2 indexes separated by a colon to grab all values up to, but not including, the last index. 

#TODO: Ommitting an index on either side of the colon is the same as saying 'everything on this side'

print(names[:2]) #? Prints the same as the above

print(names[2:]) #? Prints 'Sean' and onward

#TODO: Get the length of a list

print('Length of "names" list: ' + str(len(names))) 
print(names.__len__()) #? Random weird way to get it, not shown in book - just randomly found it myself. Not sure what underscores mean

print(23.85 + 22.07 + 5.83)

#TODO: Using for loops with lists

for i in range(4):
    print(i)

#TODO: Iterate over the indexes of a list

supplies = ['pens','pencils','paper','staples','books','binders','backpacks']

for i in range(len(supplies)):
    print('Index ' + str(i) + ': ' + supplies[i])

#TODO: Using *in* or *not in* operators

mySupply = input('Type in a string to find out if we have a supply in stock: ')

if mySupply in supplies:
    print('We have that in stock!')
else:
    print('Sorry, we do not have that.')

#TODO: Multiple assignment - assign mutliple variables a value simultaneously by using the values in a list

me = ['tall','dark','handsome'] #? If I was to add another item to this list and try the multiple assignment with only 3 variables still, it would throw an error.
height,color,appearance = me

print(str(height) + ' ' + str(color) + ' ' + str(appearance))

#* Methods are called on values, while functions are simply called
#? e.g. name.title() = method; str(appearance) = function

#TODO: Inserting/appending items to a list
#* Insert

stuff = [1,2,3,5]
stuff.insert(3, 4) #? With the insert method, you need an index and a value, separated by commas in the parentheses
print(stuff) #? This will show you that the value 4 was added at position 3 from the above line of code


#* Append

stuff.append('six') #? Adds 'six' to the end of the list

#* Remove

stuff.remove('six') #? Removes 'six' from list - remove() method only removes first occurrence of item in list if there are multiple. 
