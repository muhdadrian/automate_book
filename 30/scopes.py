# Local vars cannot be used in the global scope

def spam():
    eggs = 31337
spam()
print(eggs)

# The error happens because the eggs var exists only in the local scope created when spam() is
# called. Once the program executions returns from spam, that local scope is destroyed, and there
# is no longer a var named eggs. So when your program tries to run print(eggs), Python gives you
# an error saying that eggs is not defined. This makes sense if you think about it; when the
# program execution is in the global scope, no local scopes exist, so there can't be any local
# vars. This is why only global vars can be used in the global scope.


