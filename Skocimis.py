#https://dmoj.ca/problem/coci08c1p1

L = []
k = input().split(" ")

k = list(map(int, k))

result1 = (k[1] - k[0] - 1)
result2 = (k[2] - k[1] - 1)

if result1 > result2:
    print(result1)
else:
    print(result2)
