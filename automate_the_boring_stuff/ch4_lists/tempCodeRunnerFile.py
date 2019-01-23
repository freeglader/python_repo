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
print(newtestlist[0])