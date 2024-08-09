import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
v = int(sys.stdin.readline().strip())

if v in numbers:
    num_count = sum(1 for number in numbers if number == v)
    print(num_count)
else:
    print(0)
