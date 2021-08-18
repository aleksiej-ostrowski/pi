#--------------------------------#
#                                #
#  version 0.0.1                 #
#                                #
#  Aleksiej Ostrowski, 2021      #
#                                #
#  https://aleksiej.com          #
#                                #
#--------------------------------#  

import mmap
from colorama import init
from termcolor import colored

what_find  = b'777777777' # pattern
const_plus = 10           # show after pattern

h = what_find.hex()

print('str:', what_find.decode())
print('hex str:', h)

with open("1kkk.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    r = mm.find(what_find)
    if r != -1:
        offset = r + len(what_find)
        print(f"pattern: {mm[r:offset].decode()}{colored(mm[offset:offset + const_plus].decode(), 'green')}")
        print('pattern is found in n =', colored(r - 1, 'red'))
    else:
        print(what_find, 'is not found')
