import sys
import math

# 소수 판별 함수
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 입력 받기
M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

# M 이상 N 이하의 소수 찾기
prime_list = [num for num in range(M, N + 1) if is_prime(num)]

if prime_list:
    prime_sum = sum(prime_list)
    prime_min = min(prime_list)
    print(prime_sum)
    print(prime_min)
else:
    print(-1)
