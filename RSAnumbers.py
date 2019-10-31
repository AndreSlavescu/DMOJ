#https://dmoj.ca/problem/ccc05j2

min = int(input())
max = int(input())

def isRSA(i):
    divisor = 0
    for j in range(1, max + 1):
        if i%j == 0:
            divisor = divisor + 1
        if divisor > 4:
            return False
    if divisor == 4:
        return True
    else:
        return False

total = 0

for i in range(min, max+1):
    if isRSA(i):
        total = total + 1

print(f"The number of RSA numbers between {min} and {max} is {total}")
