#word scrambler
#https://dmoj.ca/problem/ics4p1

from itertools import permutations
perms = [''.join(p) for p in permutations(input())]
for i in perms:
    print(i)
