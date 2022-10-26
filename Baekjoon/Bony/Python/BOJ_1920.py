import sys
input = sys.stdin.readline

numMap = {}

n = int(input())
nArr = list(input().split())
for i in range(n):
    numMap[nArr[i]] = 1

m = int(input())
mArr = list(input().split())
for i in range(m):
    if mArr[i] in numMap:
        print(1)
    else:
        print(0)
