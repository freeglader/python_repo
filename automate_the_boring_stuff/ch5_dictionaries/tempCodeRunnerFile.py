
#* setdefault() method mini program - count all the occurences of the characters in the following message:

message = 'Underneath the bridge the tarp has sprung a leak'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1
print('MESSAGE: ' + message + '\n')
print('Number of occurences for each character: \n')
print(count.items())
