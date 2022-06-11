#import os
from random import randint

# print('foi')

NUMBER_OF_ENTRIES = 7


class Rules:

    def __init__(self):
        pass

    def convert_integer_to_binary(self, integer):
        return bin(integer)[2:]


# if __name__ == '__main__':
rules = Rules()
integer_vars = []  # [0, 1, 2, 3, 4, 5, 6, 7]
binary_vars = []
for var in range(NUMBER_OF_ENTRIES):
    integer_vars.append(str(var))
    binary_vars.append(rules.convert_integer_to_binary(var).rjust(3, '0'))

print('integer_vars: ', integer_vars)
print('binary_vars: ', binary_vars)

# stapTree
for _ in range(NUMBER_OF_ENTRIES):
    value = randint(0, NUMBER_OF_ENTRIES)
    print(value)
