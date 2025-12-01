# The isX() Methods

# these methods return a Boolean value that describes the nature of the str.

# isalpha(): returns True if the str consists only of letters and isn't blank.

# isalnum(): returns True if the str consists only of letters and numbers and is not blank.

# isdecimal(): returns True if the str consists only of numeric chars and is not blank
 
# isspace(): returns True if the str consists only of spaces, tabs, and newlines and is not blank

# istitle(): returns True if the str consists only of words that begin with n uppercase letter followed by only lowercase letters.

# enter the following into the interactive shell:

print('hello'.isalpha())      
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())
print('123'.isdecimal())
print('   '.isspace())
print('This Is Title Case'.istitle())
print('This Is Title Case 123'.istitle())
print('This Is not Title Case'.istitle())
print('This Is NOT Title Case Either'.istitle())