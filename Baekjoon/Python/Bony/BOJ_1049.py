import sys
input = sys.stdin.readline

allLines = []
lines = []
allMin = 0
oneMin = 0
answer = 0

n, m = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())

    allLines.append(a)
    lines.append(b)

allMin = min(allLines)
oneMin = min(lines)

if allMin < 6*oneMin:
    answer += allMin*(n//6)
    n = n % 6

    if allMin > n*oneMin:
        answer += oneMin*n
    else:
        answer += allMin
else:
    answer += oneMin*n

print(answer)
