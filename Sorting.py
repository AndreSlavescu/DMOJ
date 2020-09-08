#https://dmoj.ca/problem/a4b1

num = int(input())
a = []

for i in range(num):
    nums = int(input())
    a.append(nums)
    
def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)  
    else:  
        return array

s = sort(a)

for i in range(len(s)):
    print(s[i])
