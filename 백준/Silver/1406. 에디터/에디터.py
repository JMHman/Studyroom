import sys

# 입력을 읽어 각 줄별로 처리
input_edit = sys.stdin.read().splitlines()
initial_str = input_edit[0]
commands_count = int(input_edit[1])

# 문자열을 리스트로 관리하고, 초기 커서 위치는 문자열의 끝
left_stack = list(initial_str)  # 커서 왼쪽의 모든 문자
right_stack = []  # 커서 오른쪽은 초기에 비어있음

# 커맨드 처리
for i in range(2, 2 + commands_count):
    command = input_edit[i].strip().split()
    if command[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())  # 왼쪽 스택에서 빼서 오른쪽 스택으로 이동
    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())  # 오른쪽 스택에서 빼서 왼쪽 스택으로 이동
    elif command[0] == 'B':
        if left_stack:
            left_stack.pop()  # 왼쪽 스택의 마지막 원소 제거
    elif command[0] == 'P':
        left_stack.append(command[1])  # 왼쪽 스택에 새 문자 추가

# 최종 문자열 조합
final_string = ''.join(left_stack + right_stack[::-1])
print(final_string)
