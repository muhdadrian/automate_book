spam = {'color': 'red', 'age': 42}

for i in spam.items():
    print(i) 
    
# when you use the keys(), values(), and items() methods, a for loop can iterate over the keys, values, or key-value pairs in a dictionary, respectively.

# the values in the dict_items value returned by the items() method are tuples of the key and value.

# if you want a true list from one of these methods, pass its list-like return value to the list() function. Go to 102