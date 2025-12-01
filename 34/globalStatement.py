# The assignment is done to the globally scoped eggs. No local eggs var is created.
def spam():
    global eggs # eggs is declared global
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)