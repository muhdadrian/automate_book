# Ending a Program Early with the sys.exit() Function

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

    # print(f"You typed {response}.") #mycode