# Local Scopes Cannot Use Vars in Other Local Scopes

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()