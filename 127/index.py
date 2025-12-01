# upper() and lower() str methods themselves return strings, you can call str methods on those returned str values as well.

# expressions that do this will look like a chain of method calls.

print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())
print('HELLO'.lower())
print('HELLO'.lower().islower())