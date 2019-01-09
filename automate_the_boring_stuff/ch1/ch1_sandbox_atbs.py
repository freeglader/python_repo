# Chapter 1 - Python Basics

#* Get user input

print("Hey, what's your name?")
name = input()
print("Nice to meet you, " + name + ".")

print("Want to know how many letters are in your name?")
response = input()

if response == "yes":
    print("There are " + str(len(name)) + " letters in your name")
elif response == "no":
    print("Well SCREW YOU!!!!!")
else:
    print("ENGLISH! DO YOU SPEAK IT?")
