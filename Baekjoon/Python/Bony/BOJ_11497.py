from collections import deque
import sys

input = sys.stdin.readline
testCase = int(input())

for _ in range(testCase):
    n = int(input())
    logs = list(map(int, input().split()))

    logs.sort()
    upDownArr = logs[0:n-1:2] + logs[-1::-2]

    nowLevel = abs(upDownArr[0] - upDownArr[n-1])
    for i in range(1, n+1):
        nowLevel = max(nowLevel, abs(upDownArr[i-1] - upDownArr[i]))

    print(nowLevel)
