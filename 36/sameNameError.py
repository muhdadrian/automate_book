def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()

# writing functions without global vars is encouraged