import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))

answer = 0
maxNum = 0
plusIndex = 0
minusIndex = 0
minus = [0]
plus = [0]

for book in books:
    if book > 0:
        plus.append(book)
    else:
        minus.append(book)

    if abs(book) > abs(maxNum):
        maxNum = book

plus.sort(reverse=True)
minus.sort()

if maxNum == plus[0]:
    plusIndex = m
    answer += plus[0]
else:
    minusIndex = m
    answer += abs(minus[0])

for i in range(plusIndex, len(plus), m):
    answer += plus[i]*2

for i in range(minusIndex, len(minus), m):
    answer += abs(minus[i])*2

print(answer)
