def changeNextS(s):
    sArr = list(s)

    for i in range(len(sArr)):
        chrNum = ord(sArr[i])
        if chrNum + 1 > 122:
            sArr[i] = chr(chrNum+1-26)
        else:
            sArr[i] = chr(chrNum+1)

    return ''.join(sArr)


code = input()
n = int(input())
words = [input() for _ in range(n)]

nextNum = 0
exitCheck = False

for i in range(26):
    for word in words:
        if word in code:
            exitCheck = True
            break

    if exitCheck == True:
        break

    nextNum += 1
    code = changeNextS(code)

print(code)
