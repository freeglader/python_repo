# Exception Handling

#? Without exception handling, your program will just crash when it gets an error. You need to create a way to make the program detect the error, handle it, then move on.

def spam(divideBy):
    return 42 / divideBy
print(spam(2))
print(spam(0))
print(spam(1)) # This last part won't get executed because the program errors out at the line above this one.

#* Errors can be handled using try & except statements

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(0))
print(spam(1))