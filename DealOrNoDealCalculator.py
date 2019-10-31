# https://dmoj.ca/problem/ccc07j3

cases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

openCases = int(input())

for i in range(0, openCases):
    casenumber = int(input())
    cases[casenumber-1] = 0

bankoffer = int(input())

total = 0

for val in cases:
    total = total+val

if total/(len(cases)-openCases) < bankoffer:
    print("deal")
else:
    print("no deal")