spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])

print('Hello, ' + spam[0])
print(f"Hello, {spam[0]}")

print('The ' + spam[1] + ' ate the ' + spam[0] + '.')
print(f"The {spam[1]} ate the {spam[0]}.")

print(spam[int(1.0)]) # if only spam[1.0] it will cause an error