# Numeric Values of Characters with the ord() and chr() Functions

# computers store info as bytes -- strings of binary numbers, which means we need to be able to convert text to numbers.

# every text character has a corresponding numeric value called a Unicode code point.

# for e.g, the numeric code point is 65 for 'A', 52 for '4', and 33 for '!'.

# you can use the ord() function to get the code point of a one-char str, and the chr() function to get the one-char str of an int code point.

# enter the following into the interactive shell:

print(ord('A'))

print(ord('4'))

print(ord('!'))

print(chr(65))

