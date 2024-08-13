import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])

def strfryCheck(i):
    str1, str2 = data[i].split()
    if sorted(str1) == sorted(str2):
        print("Possible")
    else:
        print("Impossible")

results = []
for i in range(1, N + 1):
    strfryCheck(i)