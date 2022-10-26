import sys
import re
input = sys.stdin.readline

n = int(input())

answer = []

for _ in range(n):
    s = input()
    p = re.compile('\d+')

    numArr = list(map(int, p.findall(s)))

    answer += numArr

answer.sort()

for i in range(len(answer)):
    print(answer[i])
