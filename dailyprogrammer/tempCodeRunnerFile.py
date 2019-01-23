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