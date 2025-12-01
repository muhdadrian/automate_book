# but lists don't work like in 86, because list values can change; that is, lists are mutable.

spam = [0, 1, 2, 3, 4, 5] #1
cheese = spam # the reference is being copied, not the list | #2
cheese[1] = 'Hello!' # this changes the list value. | #3
print(spam) # [0, 'Hello!', 2, 3, 4, 5]
print(cheese) # the cheese var refers to the same list.
# [0, 'Hello!', 2, 3, 4, 5]

# Python vars technically contain references to values.
