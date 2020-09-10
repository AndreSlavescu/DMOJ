#https://dmoj.ca/problem/ccc20j3

xcoor = []
ycoor = []

times = int(input())

for i in range(times):
  coor = input().split(",")
  xcoor.append(coor[0])
  ycoor.append(coor[1])

xcoor = list(map(int, xcoor))
ycoor = list(map(int, ycoor))


print(str(min(xcoor)-1)+","+str(min(ycoor)-1))
print(str(max(xcoor)+1)+","+str(max(ycoor)+1))
