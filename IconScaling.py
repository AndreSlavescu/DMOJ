#https://dmoj.ca/problem/ccc12j3

# row1 = "*x*"
# row2 = " xx"
# row3 = "* *"

# def printrow(row, scale):
#     for i in range(0, scale):
#         for c in row:
#             for k in range(0, scale):
#                 print(c, end="")
#         print()            

# scale = int(input())
# # print(scale)

# printrow(row1, scale)
# printrow(row2, scale)
# printrow(row3, scale)

scale = int(input())
print(scale)

row1 = '*'*scale + 'x'*scale + '*'*scale
row2 = ' '*scale + 'x'*scale + 'x'*scale
row3 = '*'*scale + ' '*scale + '*'*scale

for i in range(scale):
    print(row1)
for i in range(scale):
    print(row2)
for i in range(scale):
    print(row3)