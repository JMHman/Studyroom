import sys

def is_perfect_number(n):
    divisors = [1]  # 1은 모든 수의 약수
    for i in range(2, int(n**0.5) + 1):  # 2부터 n의 제곱근까지 반복
        if n % i == 0:  # i가 n의 약수라면
            divisors.append(i)  # i를 약수 리스트에 추가
            if i != n // i:  # i가 n의 제곱근이 아니라면
                divisors.append(n // i)  # n을 i로 나눈 몫도 약수 리스트에 추가
    return sum(divisors) == n, divisors  # 약수의 합이 n과 같은지 확인

while True:
    n = int(sys.stdin.readline().strip())
    
    if n == -1:
        break
    
    is_perfect, divisors = is_perfect_number(n)
    
    if is_perfect:
        print(f"{n} = {' + '.join(map(str, sorted(divisors)))}")
    else:
        print(f"{n} is NOT perfect.")