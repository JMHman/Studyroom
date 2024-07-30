import sys

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

N = int(sys.stdin.readline().strip())
numbers = list(map(int,sys.stdin.readline().strip().split()))

prime_count = 0
for number in numbers:
    if is_prime(number):
        prime_count += 1

print(prime_count)
    