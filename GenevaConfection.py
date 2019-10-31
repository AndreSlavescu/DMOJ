#https://dmoj.ca/problem/ccc14s3

tests = int(input())

for i in range(0, tests): 
    num_in_tests = int(input())
    numbers = {}
    for i in range(0, num_in_tests):
        numbers[i] = int(input())
    i = num_in_tests-1
    lake = 0
    j = -1
    branch = {}
    while i >= 0:
        if lake + 1 == numbers[i]:
            lake = numbers[i]
            i = i - 1
        elif j>=0 and lake + 1 == branch[j]:
            lake = branch[j]
            # branch.remove(j)
            j = j-1
        else:
            j = j+1
            branch[j] = numbers[i]
            i = i - 1
    failed = False 
    while j>=0:
        if lake + 1 == branch[j]:
            lake = branch[j]
            j=j-1
        else:
            failed = True
            break

    if failed:
        print("N")
    else:
        print("Y")
        



