# Importing Modules

# Python comes with a set of modules called standard library.
# Example: math module has mathematics-related functions.
# Example2: random module has random number-related functions, and so on.
# Once you import a module, you can use all the cool functions of that module. Let's try with the
# random module, which will give us access to the random.randint() function.

import random

for i in range(5):
    print(random.randint(1, 10))

# Since randint() is in the random module, you must first type random. in front of the function
# name to tell Python to look for this function inside the random module.