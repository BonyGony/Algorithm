import sys
input = sys.stdin.readline

testCase = int(input())


def prefixCheck():
    for i in range(1, len(numArr)):
        if numArr[i-1] == numArr[i][0:len(numArr[i-1])]:
            return 'NO'

    return 'YES'


for _ in range(testCase):
    numArr = []

    n = int(input())

    for i in range(n):
        numArr.append(input().strip())

    numArr.sort()

    print(prefixCheck())
