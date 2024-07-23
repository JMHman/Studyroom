import sys

x,y,z = map(int,sys.stdin.readline().strip().split())
m = 0

if x == y == z:
    m = 10000 + (x * 1000)
elif x == y or x == z:
    m = 1000 + (x * 100)
elif y == z:
    m = 1000 + (y * 100)
else:
    m = max(x,y,z) * 100
    
print(m)