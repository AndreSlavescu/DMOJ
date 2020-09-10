#https://dmoj.ca/problem/ccc02s2

from fractions import Fraction

div = int(input())
num = int(input())

result = div//num
remainder = div - num * result
newfraction = Fraction(remainder, num)


if result * num < div and result != 0 and num < div:
    print(str(result)+" "+str(newfraction))
elif num > div:
    print(str(Fraction(div, num)))
elif result == 0:
    print(str(newfraction)+"/"+str(num))
else:
    print(str(result))
