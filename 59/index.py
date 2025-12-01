# Using the enumerate() Function with Lists

# Instead of using the range(len(someList)) technique with a for loop to obtain the integer index of
# the items in the list, you can call the enumerate() function instead.

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# The enumerate() function is useful if you need both the item and the item's index in the loop's
# block.