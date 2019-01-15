
#TODO: Write a program that allows the user to enter cat names, adding them to a list. Stop the program when the user is ready.

catNames = []
keepGoing = True

while True:
    print('There are countless cats at the animal shelter. It is your job to name them! Give these cats some names now, and stop whenever you feel like it by pressing 0.')

    name = input('Name cat ' + str(len(catNames) + 1) + ', or press 0 to stop: ')
    
    try:
        if name != str(0):
            print('Naming cat ' + str(len(catNames) + 1) + ' ' + name.title() + '.\n')
            catNames += [name]
        else:
            print('Total number of cats named today: ' + str(len(catNames)))
            print('Names:')
            
            for name in catNames:
                print('  ' + name.title())
            break
    except:
        print('There was an error. Don\'t ask me what kind.')
    
