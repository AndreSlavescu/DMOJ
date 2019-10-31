#https://dmoj.ca/problem/ccc98s1

import re

lines = {}

count = int(input())
for i in range (0, count):
    lines[i] = input()

for i in range (0, count):
    result = re.sub(r'\b[a-zA-Z]{4}\b' , "****", lines[i])
    print(result)