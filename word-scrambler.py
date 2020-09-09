#word scrambler
#https://dmoj.ca/problem/ics4p1

from itertools import permutations
perms = [''.join(p) for p in permutations(input())]
for i in sorted(perms):
    print(i)
