import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int,sys.stdin.readline().strip().split()))
v = int(sys.stdin.readline().strip())

num_count = 0

num_set = set(numbers)
for a in num_set:
    if a == v:
        num_count += 1
    
if num_count == 0:
    print(num_count)
else:
    for i in numbers:
        if i == v:
            num_count+=1
    print(num_count-1)
        