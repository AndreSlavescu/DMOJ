#https://dmoj.ca/problem/ccc07j1

bowl1= int(input())
bowl2 = int(input())
bowl3 = int(input())

if (bowl1 > bowl2 and bowl1 < bowl3) or (bowl1 > bowl3 and bowl1 < bowl2):
    print(bowl1)
elif (bowl2 > bowl1 and bowl2 < bowl3) or (bowl2 > bowl3 and bowl2 < bowl1):
    print(bowl2)
else:
    print(bowl3)