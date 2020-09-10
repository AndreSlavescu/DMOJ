#https://dmoj.ca/problem/set

#https://dmoj.ca/problem/set

from collections import Counter

nums = int(input())
numlist = []

for i in range(nums):
    n = int(input())
    numlist.append(n)
    
print(len(Counter(numlist).keys()))
