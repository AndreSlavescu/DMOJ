#https://dmoj.ca/problem/ccc06j2

m = int(input())
n = int(input())

total = 0

for i in range(1, m+1):
    for j in range(i,n+1):
        if i+j == 10:
            total = total + 1 

if total == 1:
    print(f"There is {total} way to get the sum 10.")
else:
    print(f"There are {total} ways to get the sum 10.")

