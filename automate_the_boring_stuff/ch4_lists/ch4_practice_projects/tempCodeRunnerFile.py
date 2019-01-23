spam = ['apples','bananas','tofu','cats']

def listSentence(w):
    for i in w:
        if i != w[-1]:
            print(i + ', ', end = '')
        else:
            print('and ' + i,end = '')
listSentence(spam)
        