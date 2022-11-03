a = int(input())
b = int(input())
c = int(input())
totalArr = list(str(a*b*c))
numDic = {}

for i in range(10):
    ch = str(i)
    numDic[ch] = 0

for n in totalArr:
    numDic[n] += 1

for v in numDic.values():
    print(v)
