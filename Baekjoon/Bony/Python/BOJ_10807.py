num = int(input())
arr = list(map(int, input().split()))
n = int(input())
numDic = {}

for k in arr:
    if k in numDic:
        numDic[k] += 1
    else:
        numDic[k] = 1

if n in numDic:
    print(numDic[n])
else:
    print(0)
