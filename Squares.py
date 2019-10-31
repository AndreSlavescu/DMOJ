#https://dmoj.ca/problem/ccc04j1

import math

tiles = int(input())

maxLengthSquare = math.sqrt(tiles)

maxLength = math.floor(maxLengthSquare)

print(f"The largest square has side length {maxLength}.")