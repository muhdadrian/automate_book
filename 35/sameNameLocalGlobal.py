# If you want to modify the value stored in a global var from in a function, you must use
# a 'global' statement on that var.

def spam():
    global eggs #1
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local | # 2

def ham():
    print(eggs) # this is the global | # 3

eggs = 42 # this is the global
spam()
print(eggs)