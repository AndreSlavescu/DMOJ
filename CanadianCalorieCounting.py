#https://dmoj.ca/problem/ccc06j1

burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

burgerOpts = [461, 431, 420, 0]
sideOpts = [100, 57, 70, 0]
drinkOpts = [130, 160, 118, 0]
dessertOpts = [167, 266, 75, 0]

total = burgerOpts[burger-1] + sideOpts[side-1] + drinkOpts[drink-1] + dessertOpts[dessert-1]

print(f"Your total Calorie count is {total}.")
