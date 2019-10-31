#https://dmoj.ca/problem/ccc96s1

numberofnumbers = int(input())

for j in range(0, numberofnumbers):

    number = int(input())

    sum = 1

    for i in range(2, number):
        if number%i == 0:
            sum = sum + i 
    if sum > number:
        print(f"{number} is an abundant number.")
    elif sum < number:
        print(f"{number} is a deficient number.")
    else:
        print(f"{number} is a perfect number.")