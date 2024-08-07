import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
x = int(sys.stdin.readline().strip())

number_set = set(numbers)
count = 0

for num in numbers:
    target = x - num
    # Set을 검사하여 target이 존재하고, num이 target보다 작은 경우만 카운트
    if target in number_set and target > num:
        count += 1

# 결과 출력
print(count)
