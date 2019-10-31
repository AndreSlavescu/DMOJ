#https://dmoj.ca/problem/ccc05j1

daytime = int(input())
evening = int(input())
weekend = int(input())

planA = 0
if daytime > 100:
    planA = (daytime-100)*25
planA = planA + evening*15 + weekend*20

planB = 0
if daytime > 250:
    planB = (daytime-250)*45
planB = planB + evening*35 + weekend*25

print(f"Plan A costs {planA/100}")
print(f"Plan B costs {planB/100}")

if planA > planB:
    print("Plan B is cheapest.")
elif planA < planB:
    print("Plan A is cheapest.")
else:
    print("Plan A and B are the same price.")