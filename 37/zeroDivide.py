# Exception Handling: you want the program to detect errors, handle them, and then continue
# to run.

def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# Errors can be handled with try and except statements. See the next code.