# The upper() and lower() methods are helpful if you need to make a case-insensitive comparison. 

# the str 'great' and 'GREat' are not equal to each other. Therefore, we need to convert the str to lowercase first

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')

else:
    print('I hope the rest of your day is good.')