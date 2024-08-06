import sys

room = str(sys.stdin.readline().strip())

num_set = 0

digit_count = [0] * 10
for char in room:
    digit_count[int(char)] += 1
    
six_nine_count = digit_count[6] + digit_count[9]
digit_count[6] = digit_count[9] = (six_nine_count + 1) // 2

num_set = max(digit_count)

print(num_set)