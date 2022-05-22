# ----------------------------------#
#                                   #
#  version 0.0.2                    #
#                                   #
#  Aleksiej Ostrowski, 2021 - 2022  #
#                                   #
#  https://aleksiej.com             #
#                                   #
# ----------------------------------#  

import mmap
# from colorama import init
# from termcolor import colored

table = '''
| Pattern | First matching in ***pi***, n | First matching in ***e***, n |
| --- | --- | --- |
'''

N = 10

with open("pi1b.txt", "r+b") as f_pi, \
     open("e1b.txt", "r+b") as f_e:
    with mmap.mmap(f_pi.fileno(), 0, access=mmap.ACCESS_READ) as mm_pi, \
         mmap.mmap(f_e.fileno(), 0, access=mmap.ACCESS_READ) as mm_e:
        for NUMBER in (b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9'):
            patterns = [NUMBER * x for x in range(1, N + 1)]
            # print(patterns)

            # h = what_find.hex()
            # print('str:', what_find.decode())
            # print('hex str:', #h)

            mm_pi.seek(1)
            mm_e.seek(1)

            for p in patterns:

                r = mm_pi.find(p)
                table += '| `' + p.decode() + '` | `' 
                if r != -1:
                    # const_plus = 10  # show after pattern
                    # offset = r + len(p)
                    # print(f"pattern: {mm[r:offset].decode()}{colored(mm[offset:offset + const_plus].decode(), 'green')}")
                    # print('n after 3. =', colored(r - 1, 'red'))
                    table += str(r - 1)
                else:
                    table += 'not found'

                r = mm_e.find(p)
                table += '` | `' 
                if r != -1:
                    table += str(r - 1)
                else:
                    table += 'not found'

                table +=  '` |\n'
print(table)
