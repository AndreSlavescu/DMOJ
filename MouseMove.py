#https://dmoj.ca/problem/ccc05s2
import sys

line = input()
(width, height) = line.split()

width = int(width)
height = int(height)

# print("test")
# print(width, height)

cur_x = 0 
cur_y = 0 

while True:
    line = input()
    (rel_x, rel_y) = line.split()
    rel_x = int(rel_x)
    rel_y = int(rel_y)
    
    # print(rel_y, rel_y)

    if rel_x == 0 and rel_y == 0:
        sys.exit()

    temp_x = cur_x + rel_x
    temp_y = cur_y + rel_y

    if temp_x > width:
        temp_x = width
    elif temp_x < 0:
        temp_x = 0

    if temp_y > height:
        temp_y = height
    elif temp_y < 0:
        temp_y = 0

    cur_x = temp_x
    cur_y = temp_y

    print(cur_x, cur_y)