from sys import stdin, stdout
from itertools import combinations

dwarves = []

for i in range(9):
    dwarves.append(int(stdin.readline()))

dwarves.sort()

for d in list(combinations(dwarves, 7)):
    sum_dwarves = sum(d)
    if sum_dwarves == 100:
        for dwarf in d:
            stdout.write(str(dwarf)+'\n')
        break
