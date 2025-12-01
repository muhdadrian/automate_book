# Passing References

# when a function is called, the values of the args are copied to the para vars.
# for lists and dictionaries, this means a copy of the reference is used for the para.

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) # [1, 2, 3, 'Hello']

# when eggs() is called, a return value is not used to assign a new value to spam. 
# Instead, it modifies the list in place, directly.
# spam and someParameter contain separate references, but they both refer to the same list. 
# This is why the append('Hello') method call inside the function affects the list even after the function call has returned.