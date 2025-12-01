# if you have only one value in your tuple, you can indicate this by placing a trailing comma after the value inside the parentheses.
# it's fine to have a trailing comma after the last item in a list or tuple in Python

print(type(('hello',)))
print(type(('hello')))
print(type(['hello',]))

# you can use tuples to convey to anyone reading your code that you don't intend for that sequence of values to change.
# if you need an ordered sequence of values that never changes, use a tuple.
# a 2nd benefit of using tuples instead of lists: Python can implement some optimizations that make code using tuples slightly faster than code using lists.