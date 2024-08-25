import sys
input = sys.stdin.read

def solve():
    data = input().split()
    n = int(data[0])
    sequence = list(map(int, data[1:]))
    
    stack = []
    result = []
    current = 1
    
    for num in sequence:
        while current <= num:
            stack.append(current)
            result.append('+')
            current += 1
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            print("NO")
            return
    
    for op in result:
        print(op)

solve()
