import sys
import math

def prime_factors(n):
    factors = []
    
    # 2부터 시작해서 나누기
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # 3 이상의 홀수로 나누기
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # 남은 소수 처리
    if n > 2:
        factors.append(n)
    
    return factors

# 입력 받기
N = int(sys.stdin.readline().strip())

# N이 1인 경우 아무것도 출력하지 않음
if N != 1:
    factors = prime_factors(N)
    for factor in factors:
        print(factor)
