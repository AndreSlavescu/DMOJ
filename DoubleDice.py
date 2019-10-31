A = 100
D = 100

totalRounds = int(input())

while totalRounds > 0:
    (ar, dr) = input().split()

    ar = int(ar)
    dr = int(dr)
    totalRounds = totalRounds - 1    
    if ar > dr:
        D = D - ar
    elif ar < dr:
        A = A - dr

print(A)
print(D)