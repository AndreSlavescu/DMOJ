#https://dmoj.ca/problem/ccc14j2

votecount = int(input())
votes = input()
a = 0
b = 0

for i in range(0, votecount):
    if votes[i] == "A":
        a = a+1
    else:
        b = b+1

if a == b:
    print("Tie")
elif a > b:
    print("A")
else: 
    print("B")

