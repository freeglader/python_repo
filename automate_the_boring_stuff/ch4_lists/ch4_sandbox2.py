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