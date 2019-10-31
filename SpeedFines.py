#https://dmoj.ca/problem/ccc12j1

sl = int(input())
ys = int(input())

diff = ys - sl

if diff >=31:
    print("You are speeding and your fine is $500.")
elif diff >= 21:
    print("You are speeding and your fine is $270.")
elif diff >= 1:
    print("You are speeding and your fine is $100.")
else:
    print("Congratulations, you are within the speed limit!")
