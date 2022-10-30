arr = list(input())
numDic = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
}

for n in arr:
    if n == '9':
        if numDic['9'] > numDic['6']:
            numDic['6'] += 1
        else:
            numDic['9'] += 1
    elif n == '6':
        if numDic['6'] > numDic['9']:
            numDic['9'] += 1
        else:
            numDic['6'] += 1
    else:
        numDic[n] += 1

print(max(list(numDic.values())))
