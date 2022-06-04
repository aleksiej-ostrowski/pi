# ----------------------------------#
#                                   #
#  version 0.0.1                    #
#                                   #
#  Aleksiej Ostrowski, 2021 - 2022  #
#                                   #
#  https://aleksiej.com             #
#                                   #
# ----------------------------------#

import mmap

table = """
| Pattern | All matching in ***π***, n | All matching in ***e***, n |
| --- | --- | --- |
"""

counts_pi = {str(k): 0 for k in range(0, 10)}
counts_e = {str(k): 0 for k in range(0, 10)}

with open("pi1b.txt", "r+b") as f_pi:
    with mmap.mmap(f_pi.fileno(), 0, access=mmap.ACCESS_READ) as mm_pi:
        mm_pi.seek(2)
        while True:
            b = mm_pi.read(1).decode()
            if b in ["\n", ""]:
                break
            counts_pi[b] += 1

with open("e1b.txt", "r+b") as f_e:
    with mmap.mmap(f_e.fileno(), 0, access=mmap.ACCESS_READ) as mm_e:
        mm_e.seek(2)
        while True:
            b = mm_e.read(1).decode()
            if b in ["\n", ""]:
                break
            counts_e[b] += 1

for (k1, v1), (k2, v2) in zip(counts_pi.items(), counts_e.items()):
    if k1 == k2:
        table += "| `" + str(k1) + "` | `" + str(v1) + "` | `" + str(v2) + "` |\n"

print(table)
