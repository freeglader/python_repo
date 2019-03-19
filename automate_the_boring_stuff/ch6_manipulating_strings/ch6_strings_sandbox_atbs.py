
#? Multiline strings: use them instead of \n to make your life easier when you need a lot of new lines / tabs, etc

print('''       Here is a multiline string.

I\'m going to keep typing and doing some new lines and thangs.

Whatcha gonna do bout it?   ''')

#? Slicing strings: every string is basically like a list of characters, accessible with index values.

stringSliceTest = 'This is a string to slice up boi'
slicedUpString = stringSliceTest[0:7] #? Should get the following: 'This is'
print(slicedUpString)
print('Index 7: ' + stringSliceTest[7])

print('slicedUpString last char: ' + slicedUpString[-1])

#? Using 'in' and 'not in' operators: 

if 'hello' in 'hello world':
    print('True')
else:
    print('False')

if 'hello' in 'HELLO world':
    print('True')
else:
    print('False')

