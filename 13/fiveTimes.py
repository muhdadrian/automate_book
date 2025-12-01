# for Loops and the range() Function

# The while loop keeps looping while its condition is True(which is the reason for its name), but
# what if you want to execute a block of code only a certain number of times? You can do this with
# a for loop statement and the range() function.

# In code, a for statement looks something like for i in range(5): and includes the following:

# The for keyword
# A var name
# The in keyword
# A call to the range() method with up to three integers passed to it
# A colon
# Starting on the next line, an indented block of code (called the for clause)

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# You can use continue and break statements only inside while and for loops. It will output error
# if you use them elsewhere.

# Below is my code:

# print('My name is:')
# for i in range(5):
#     print(f'Jimmy Five Times (' f'{i})')