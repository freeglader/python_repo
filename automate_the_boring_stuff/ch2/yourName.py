name = ''
count = 0

while name != 'your name':
    print('Please type your name:\n')
    name = input()
    count += 1
if count >= 10:
    print('Holy frick, how are humans this stupid? It took you a whopping ' + str(count) + ' tries. I literally told you exactly what to type! You don\'t see me making mistakes like that!')
elif count >= 5: 
    print('Hey you finally got it! Man, that took you longer than I thought it would. You had to guess ' + str(count) + ' times.')
else:
    print('Good job! You figured out my riddle. Not bad for a meat bag. It only took you ' + str(count) + ' tries.')
