import sys

def KeyLoger(pw_log):
    left_stack = []
    right_stack = []
    for char in pw_log:
        if char == '<':
            if left_stack:  # 커서를 왼쪽으로 옮길 수 있으면
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack: # 커서를 오른쪽으로 옮길 수 있으면
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:  # 커서를 왼쪽으로 옮길 수 있으면
                left_stack.pop()
        else:
            left_stack.append(char)
    result = ''.join(left_stack + right_stack[::-1])
    print(result)

loop_num = int(sys.stdin.readline().strip())

for _ in range(loop_num):
    pw_logs = sys.stdin.readline().strip()
    KeyLoger(pw_logs)
    
    