# TRY IT YOURSELF

#* Exercise 2-3: Personal Message

# TODO: Store a person's name in a variable, and print a message to that person. Your message should be something simple, such as, "Hello Eric, would you like to learn some Python today?"

firstname = 'Kurt'
lastname = 'Cobain'

print('Hey ' + firstname + ', how are you today?')

#* Exercise 2-4: Name Cases

# TODO: Store a person's name in a var, then print their name in lowercase, uppercase, and titlecase

firstname = 'kurt'
lastname = 'cobain'

print(firstname + ' ' + lastname)
print(firstname.title() + ' ' + lastname.title())

#*  2-5: Famous Quote

# TODO: Find a quote from someone you admire. Print the quote and the name of its author. E.g. Albert Einstein once said, blah blah blah

fullname = firstname.title() + ' ' + lastname.title()
print('In a controversial song, ' + fullname + ' sang the lyrics "rape meEeEeeeeEEe!!!!"')

#* Exercise 2-6: Famous Quote 2

# TODO: Repeat ex 2-5, but store the famous person's name in a var & the message in a var called message

quote = 'In a controversial song, ' + fullname + ' sang the lyrics "rape meEeEeeeeEEe!!!!"'

print(quote)

#* Exercise 2-7: Stripping Names

# TODO: Store a person's name, include some whitespace, & make sure you use each character combination "\t" and "\n" at least once. Print the name once, showing the whitespace, then use the stripping functions.

spacename = ' bob '
print(spacename + '\n')

# The following code would have printed bob with a tab in front of it, but by enclosing everything in another set of parentheses and adding .strip() to the end, even tabbed whitespace is stripped away
print(('\t' + spacename.strip()).strip())



