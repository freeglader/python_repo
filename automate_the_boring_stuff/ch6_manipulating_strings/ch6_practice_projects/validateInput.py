# create a loop that never ends until a user enters the correct input
# they need to enter their name as a number, and if it's anything else it will continue to prompt

while True:
  age = input('Please enter your age: ')
  if age.isdecimal():
    print('Age entered: ' + str(age))
    break
  print('\nEnter your age as an integer\n')

  # prompt user to enter a valid password (letters and numbers only)

while True:
    password = input('Please enter a password (letters/numbers only): ')
    if password.isalnum():
        print('*' * len(password) + '\n... password updated')
        break
    print('Password must be alphanumeric')
