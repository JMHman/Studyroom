import sys

A,B = map(int, sys.stdin.readline().strip().split())
C = int(sys.stdin.readline().strip())

D = B + C

if D >= 60:
    A += D // 60
    D = D % 60
    
A = A % 24

print(A,D)
    