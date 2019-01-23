# [2019-01-14] Challenge #372 [Easy] Perfectly balanced

#TODO: Given a string containing only the characters x and y, find whether there are the same number of xs and ys.

'''
balanced("xxxyyy") => true
balanced("yyyxxx") => true
balanced("xxxyyyy") => false
balanced("yyxyxxyxxyyyyxxxyxyx") => true
balanced("xyxxxxyyyxyxxyxxyy") => false
balanced("") => true
balanced("x") => false
'''

#? Optional bonus
#? Given a string containing only lowercase letters, find whether every letter that appears in the string appears the same number of times. Don't forget to handle the empty string ("") correctly!

#* Note that balanced_bonus behaves differently than balanced for a few inputs, e.g. "x".

'''
balanced_bonus("xxxyyyzzz") => true
balanced_bonus("abccbaabccba") => true
balanced_bonus("xxxyyyzzzz") => false
balanced_bonus("abcdefghijklmnopqrstuvwxyz") => true
balanced_bonus("pqq") => false
balanced_bonus("fdedfdeffeddefeeeefddf") => false
balanced_bonus("www") => true
balanced_bonus("x") => true
balanced_bonus("") => true
'''

def getStr():
    countX = 0
    countY = 0

    #? Get string of x's and y's 
    uString = str(input('Please provide a string consisting of only xs or ys: '))
    #? Count occurences of both chars
    
    for i in uString:
        if i.lower() == 'x':
            countX += 1
        elif i.lower() == 'y':
            countY += 1
        else:
            print('You screwed up, and I am too lazy to write proper error handling. Too bad!!')
            break
    if countY == countX:
        print('The number of xs was equal to the number of ys.\nXs: ' + str(countX) + '\nYs: ' + str(countY))
    else:
        print('Xs and Ys were not equal.\nXs: ' + str(countX) + '\nYs: ' + str(countY))

getStr()




words = 'xxxxyyyy'
print(words)
words = words.split()
print(words)
words.

