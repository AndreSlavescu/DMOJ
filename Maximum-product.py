#https://dmoj.ca/problem/dmpg15b4

import sys

times = int(input())

numlist = []
negnums = []
zeroes = []

for i in range(times):
  nums = int(input())
  if nums > 0:
    numlist.append(nums)
  elif nums < 0 : 
    negnums.append(nums)
  else: 
    zeroes.append(nums)

if len(numlist) == 0 and 0 in zeroes:
    print(0)
    sys.exit()
elif len(numlist) == 0 and len(negnums) == 1:
  print(negnums[0])
  sys.exit()
  
if len(negnums)%2 != 0:
  negnums.remove(max(negnums))

for i in negnums:
  numlist.append(abs(i))

product = 1

for i in numlist:
  product = product * i

if 0 not in numlist:
  print(product)
elif 0 in numlist and len(numlist) < 3:
  print(0)
else:
  print(0)
