# here is a short program that counts the number of occurences of each letter in a string.

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0) #1
    #count[character] = count[character] + 1 #2
    count[character] += 1 #2

print(count) 

# the program loops over each character in the message var's string, counting how often each character appears.

# the setdefault() method calls #1 ensures that the key is in the count dictionary (with a default value of 0) so the program doesn't throw a KeyError error when count[character] = count[character] + 1 is executed #2. 

# from the output, you can see that:
# 1. the lowercase letter c appears 3 times
# 2. the space character appears 13 times
# 3. the uppercase letter A appears 1 time

# this program will work no matter what string is inside the message var, even if the string is millions of characters long!

