#https://dmoj.ca/problem/ccc12j4

k = int(input())
encrypted_string = input()
for p in range(len(encrypted_string)):
    s = 3*(p+1) + k
    c = encrypted_string[p]
    newC = ord(c)-s
    # print(newC)
    if newC < ord('A'):
        newC = ord('Z') - (ord('A') - newC)+1
    # print(newC, ord('A'), ord('Z'))
    print(chr(newC), end="") 