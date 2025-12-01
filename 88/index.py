# Identity and the id() Function

# you may ask why the weird behaviour with mutable lists in the previous section doesn't happen with immutable values like ints and strs. We can use Python's id() function to understand this.

# All values in Python have a unique identity that can be obtained with the id() function:

print(id('Howdy')) # The returned number will be different on your machine.

# when Python runs id('Howdy'), it creates the 'Howdy' str in the computer's memory. 
# The numeric memory address where the str is stored is returned by the id() function.
# Python picks this address based on which memory bytes happen to be free on your computer at the time, so it'll be different each time you run this code.