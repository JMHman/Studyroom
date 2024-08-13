import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])

results = []
for i in range(1, N + 1):
    str1, str2 = data[i].split()
    if sorted(str1) == sorted(str2):
        results.append("Possible")
    else:
        results.append("Impossible")

for result in results:
    print(result)