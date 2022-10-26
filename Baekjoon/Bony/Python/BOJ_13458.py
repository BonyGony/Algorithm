import math

n = int(input())
people = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0

for i in range(n):
    num = people[i]
    num -= b
    answer += 1

    if num <= 0:
        continue

    answer += math.ceil(num/c)

print(answer)
