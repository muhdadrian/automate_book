# you can use a dictionary with the names as keys and the birthdays as values.

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'} #1

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays: #2
        print(birthdays[name] + ' is the birthday of ' + name) #3
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday #4
        print('Birthday database updated.') 

#1 -- you create an initial dictionary and store it in birthdays.

#2 -- you can see if the entered name exists as a key in the dictionary with the 'in' keyword. 

#3 -- If the name is in the dictionary, you access the associated value using square brackets.

#4 -- if not, you can add it using the same square bracket syntax combined with the assignment operator.

# When you run the program. Enter:
# Alice
# Eve
# Dec 5
# Eve

# All the data you enter in this program is forgotten when the program terminates. You'll learn later how to save the data to files.