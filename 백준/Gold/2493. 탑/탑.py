import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
heights = list(map(int, data[1:]))

# 수신 탑의 위치를 저장할 리스트
receivers = [0] * N

# 스택에는 (탑의 인덱스, 탑의 높이)를 저장
stack = []

for i in range(N):
    # 현재 탑의 높이보다 낮은 탑은 스택에서 제거
    while stack and stack[-1][1] < heights[i]:
        stack.pop()
    # 스택이 비어있지 않다면, 스택의 맨 위 탑이 수신 탑
    if stack:
        receivers[i] = stack[-1][0] + 1  # 인덱스는 0부터 시작하므로 +1
    # 현재 탑을 스택에 추가
    stack.append((i, heights[i]))

# 결과 출력
print(" ".join(map(str, receivers)))
