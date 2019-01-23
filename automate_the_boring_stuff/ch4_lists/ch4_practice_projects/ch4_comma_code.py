# Chapter 4 - Comma Code 

#TODO: take a list like the following:
#TODO: spam = ['apples','bananas','tofu','cats']
#TODO: Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with 'and' inserted before the last item. e.g. passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. Function should be able to work with any list value passed to it.

spam = ['apples','bananas','tofu','cats']

def listSentence(w):
    for i in w:
        if i != w[-1]:
            print(i + ', ', end = '')
        else:
            print('and ' + i,end = '')
listSentence(spam)
        

