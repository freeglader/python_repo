# Chapter 1 - Python Basics

#* Get user input

print("Hey, what's your name?")
name = input()
print("Nice to meet you, " + name + ".")

print("Want to know how many letters are in your name?")
response = (input()).lower() # I enclosed this input() method in parentheses and applied the lower() method to it to ensure user input is understood regardless of the case

if response == "yes":
    print("There are " + str(len(name)) + " letters in your name")
elif response == "no":
    print("Well SCREW YOU!!!!!")
else:
    print("ENGLISH! DO YOU SPEAK IT?")

#* While statements

age = 0

while age < 100:
    print('Another year passes. You feel older and sapped of energy, inching closer and closer to your death.')
    age += 1
    print('**Age is now ' + str(age) + '**')
if age == 100:
    print('"FINALLY!!" The reaper said, and stuffed your pathetic soul into his death sack as what little life you had left eeked out of your wrinkled meat sack of a body.')
