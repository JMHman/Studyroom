import sys
import string

in_put = sys.stdin.readline().strip()
alphabet_list = list(string.ascii_lowercase)

alphabet_count = {}
for char in alphabet_list:
    alphabet_count[char] = 0

for char in in_put:
    if char in alphabet_count:
        alphabet_count[char] += 1

result = []
for char in alphabet_list:
    result.append(str(alphabet_count[char]))

print(' '.join(result))
