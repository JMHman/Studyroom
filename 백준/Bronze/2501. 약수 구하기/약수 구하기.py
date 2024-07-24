import sys

n,k = map(int,sys.stdin.readline().strip().split())
a = []
# ZeroDivisionError를방지하기 위해 (1,n+1) 옵션을 넣었다
for x in range(1, n + 1):
    if n % x == 0:
        a.append(x)
    x+=1
if len(a) >= k:
    print(a[k-1])
else:
    print(0)