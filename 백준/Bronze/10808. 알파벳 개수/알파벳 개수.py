import sys

# 입력 받기
input_str = sys.stdin.readline().strip()

# 알파벳 소문자의 빈도를 저장할 리스트 초기화 (길이 26, 초기값 0)
alphabet_count = [0] * 26

# 문자열을 순회하면서 각 알파벳의 빈도를 증가
for char in input_str:
    alphabet_count[ord(char) - ord('a')] += 1

# 결과 출력
print(' '.join(map(str, alphabet_count)))
