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

what_find = b'777777777'
const_plus = 10

h = what_find.hex()

print('str:', what_find.decode())
print('hex str:', h)

with open("1kkk.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    r = mm.find(what_find)
    if r != -1:
        # print('find in n =', r - 1, 'what =', mm[r:r + len(what_find) + const_plus].decode())
        print('find in n =', r - 1, f"what = {mm[r:r + len(what_find)].decode()}{colored(mm[r + len(what_find): r + len(what_find) + const_plus].decode(), 'red')}")
    else:
        print('nothing found')
