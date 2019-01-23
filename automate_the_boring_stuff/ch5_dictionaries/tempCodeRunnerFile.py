# Chapter 5 - Dictionaries and Structuring Data

#* Dictionaries are created with curly braces

myFaves = {'food': 'orange chicken', 'drink': 'diet coke', 'artist': 'travis scott', 'book': {'title': 'Pimp: The Story of My Life', 'author': 'Iceberg Slim'}} 

print(myFaves)

print('My favorite book is: ' + myFaves['book']['title'] + '. The author is known as ' + myFaves['book']['author'] + '.')