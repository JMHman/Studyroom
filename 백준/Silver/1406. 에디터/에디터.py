import sys

# 초기 문자열 읽기
initial_string = sys.stdin.readline().strip()
# 명령어 개수 읽기
command_count = int(sys.stdin.readline().strip())

# 커서를 관리할 두 개의 스택 사용 (좌측 스택, 우측 스택)
left_stack = list(initial_string)  # 커서 왼쪽의 모든 문자를 포함
right_stack = []  # 커서 오른쪽의 문자는 초기에 비어 있음

# 명령어 처리
for _ in range(command_count):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'L':
        if left_stack:  # 커서를 왼쪽으로 옮길 수 있으면
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':
        if right_stack:  # 커서를 오른쪽으로 옮길 수 있으면
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':
        if left_stack:  # 커서 왼쪽의 문자 삭제
            left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])  # 커서 왼쪽에 문자 추가

# 최종 문자열 구성
# 왼쪽 스택은 그대로, 오른쪽 스택은 뒤집어서 합치기
result = ''.join(left_stack + right_stack[::-1])
print(result)
