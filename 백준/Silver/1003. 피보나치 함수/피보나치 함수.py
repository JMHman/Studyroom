def fibonacci_counts(n):
    # 피보나치 수의 출력 횟수를 저장할 리스트
    counts = [(1, 0), (0, 1)]  # (0의 출력 횟수, 1의 출력 횟수)
    
    for i in range(2, n + 1):
        count_0 = counts[i-1][0] + counts[i-2][0]
        count_1 = counts[i-1][1] + counts[i-2][1]
        counts.append((count_0, count_1))
    
    return counts

def main():
    # 테스트 케이스의 수를 입력받습니다.
    T = int(input())
    cases = [int(input()) for _ in range(T)]
    
    # 최대 N을 찾습니다.
    max_n = max(cases)
    
    # 피보나치 수의 출력 횟수를 미리 계산합니다.
    counts = fibonacci_counts(max_n)
    
    # 각 테스트 케이스에 대해 결과를 출력합니다.
    for n in cases:
        print(counts[n][0], counts[n][1])

if __name__ == "__main__":
    main()
