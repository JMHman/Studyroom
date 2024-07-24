import sys

input = sys.stdin.read
data = input().strip().split("\n")

for line in data:
    a, b = map(int, line.split())
    
    if a == 0 and b == 0:
        break

    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')
