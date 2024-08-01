import sys

# 입력 받기
A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

# 곱셈 수행
result = A * B * C

result_str = str(result)

# 숫자 빈도 카운트
digit_count = {}
for i in range(10):
    digit_count[str(i)] = 0

    
for char in result_str:
    digit_count[char] += 1

# 결과 출력
for i in range(10):
    print(digit_count[str(i)])
