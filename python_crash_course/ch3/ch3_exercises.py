# Chapter 3 "Try it yourself" questions

#*: 3-4: Guest List

#TODO: Make a list of 3 people you want to invite to dinner & send them a message

invitees = ['bob','tom','joe']
message = 'Hi ' + invitees[0].title() + ', wanna go get dinner?'

print(message)

uninvited = invitees.pop()
uninvited_message = '\nUnfortunately, we had to uninvite ' + uninvited.title() + ' because of his erratic behavior recently.\nHe was arrested yesterday after a police officer found him smearing doof on the walls at a department store and writing Python code in it with his fingers.'

print(uninvited_message)

invitees.append('kurt')
invitees.append('dave')
invitees.append('thom')

print('\n**DINNER UPDATE**\n\tHello all, I hope you''re doing well. I have decided to invite three new people over:\n' + invitees[-1].title() + ', ' + invitees[-2].title() + ', ' + invitees[-3].title() + '.\nPlease let me know if anyone takes issue with the addition of these fine folks for dinner.')