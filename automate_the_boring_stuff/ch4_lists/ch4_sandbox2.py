# Chapter 4 - List-like Types: Strings and Tuples

#* Use a string like a list

name = 'Josh'

print(name[0]) #? Prints first letter. Think of name var like a list made up of single text chars
print(name[0:3]) #? Grab a slice of characters

for i in name:
    print('*** ' + i + ' ***')

#* List = mutable - can have values added, removed, changed

doof = ['snarf','shope','ween']
doof[2] = 'storf'
print(doof[2])

#* String = immutable - cannot be changed

#name[0] = 'M' #? Throws an error
print(name[0])

#* Use slices on strings to "mutate" the string

nameTwo = name[0:3] + 'ia' + name[-1] #? Slices chars off "Josh", grabbing "jos" for the beginning & adding ia + "h", to make "Josiah"
print(nameTwo)

#* Using copy module you can copy mutable values like list or dictionary
import copy

#? Checking the difference between copy & no copy

testlist = [1,2,3,4,5]

newtestlist = testlist
newtestlist[0] = 5
print(testlist) #? Assigning a list to another list doesn't make them separate - the values in testlist are changed when changing newtestlist
print(newtestlist)

testlist[-1] = 'fart'
print(newtestlist[-1])

#? Here's the version using the copy module

testlist = [1,2,3,4,5]
newtestlist = copy.copy(testlist)
testlist[0] = 'boofer'
print(newtestlist[0])  #? Output is the value 1, because the testlist was copied, totally separated, and placed into a new list. 

#TODO: the "deepcopy()" method copies lists + their nested lists


