# if you want to modify the original list in eggs to contain [4, 5, 6] from [1, 2, 3]:

eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs) # [4, 5, 6]