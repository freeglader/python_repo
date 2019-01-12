def jail(guilty):
    if guilty == True:   
        print('After a long trial, the judge has found you guilty of dropping a deuce in the slide at a children\'s playground. You"ve been escorted to the jail, and the officer needs some information.\n')
        name = input('What is your name?\n')
        print('\nHi, ' + name + '.')
        age = input('\nHow old are you? - type a number, please. No strings here.\n')
        eyes = input('\nAnd your eye color?\n')
        print('\nAlright, so we\'ve got a ' + name + ' here, age ' + str(age) + ', with ' + eyes + ' eyes.\nInto the slammer you go.\n*Jail door grates shut*\n')
    else:
        print('After a long trial, you have been found not guilty of taking a shite in public. During the investigation, they took DNA samples of the dog logs and found that the butt truffles were planted in the slide by a local vagrant, Jimmy. This was later confirmed by camera footage of Jimmy pressing a loaf, leaving behind a few keester cakes and a shitsicle for disturbed parents to find later that day. As the jury watched Jimmy sprout a tail on that fateful day, there was no question he"d be planting his potatoes behind bars for the rest of his days.')
jail(True)
jail(False)