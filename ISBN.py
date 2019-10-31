#https://dmoj.ca/problem/ccc09j1

part = 9*1+7*3+8*1+0*3+9*1+2*3+1*1+4*3+1*1+8*3

n1 = int(input())
n2 = int(input())
n3 = int(input())

total = part + n1*1+n2*3+n3*1

print("The 1-3-sum is " + str(total))