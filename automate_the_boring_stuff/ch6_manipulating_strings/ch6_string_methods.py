# startswith() endswith() methods

spam = ['Alan', 'Dallin', 'Marian', 'Pan','4chan']

for i in spam:
    if i.endswith('an'):
        print('Sweet!')
        print(i + '\n')
    else:
        print('Not sweet.')
        print(i + '\n')

# join() and split() methods

#? join() method is called on a string (delimiter), gets passed a list of strings, and returns a concatenated string

spam = ['My','favorite','food','is','pie']
print(' '.join(spam))