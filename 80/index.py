# Although a list value is mutable, the second line in the following code does not modify
# the list eggs:

eggs = [1, 2, 3]
eggs = [4, 5, 6]
print(eggs)

# The list value in eggs isn't being changed here; rather, an entirely new and different list value
# ([4, 5, 6]) is overwriting the old list value ([1, 2, 3]).