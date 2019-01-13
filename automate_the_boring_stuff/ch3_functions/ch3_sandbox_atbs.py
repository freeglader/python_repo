# Chapter 3 - Functions

#* Creating a Function

def hello():
    print('Hello world!')
    print('How are you?')

hello()  

#* Functions with parameters

def ageCheck(age):
    if age >= 21 and age <= 110:
        print('You\'re old enough to drink')
    elif age < 21 and age > 4:
        print('Get on out of here, you\'re not old enough to be drinking!!')
    else:
        print('Oh you think that\'s funny do you? Get out of here!')
ageCheck(25)
ageCheck(19)
ageCheck(-1)

# The following will cause an error:

def spam():
    eggs = 1337
spam()
print(eggs)

# Testing fixing the above code on my own:

def spam():
    eggs = 1337
    return eggs #? If I used print(eggs) here instead, it would return a value of None because of the print function. Assigning the function's result to the global variable eggs simply returns None when that global variable is printed.
eggs = spam()
print(eggs)

def spam():
    # eggs = 24 #? Function will print 24 if this is uncommented. If not defined locally, global var with same name takes precedence.
    global eggs #? If I use the global statement, it references the global variable
    eggs = 67 #? This is now setting the global variable of eggs to 67, when it was 42. As the global var is set to 42 before the function call, the new value will be 67 when spam is called.
    print(eggs)
eggs = 42
spam()


