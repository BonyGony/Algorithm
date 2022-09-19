import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

INF = float('INF')
homeMap = {1: [], 2: []}
answer = INF

for i in range(n):
    line = list(map(int, input().split()))

    for j in range(len(line)):
        if line[j] == 1:
            homeMap[1].append([i+1, j+1])
        elif line[j] == 2:
            homeMap[2].append([i+1, j+1])

for arr in combinations(homeMap[2], m):
    arrMin = 0

    for [hX, hY] in homeMap[1]:
        dis = INF
        for [cX, cY] in list(arr):
            dis = min(abs(cX-hX)+abs(cY-hY), dis)

        arrMin += dis

    answer = min(arrMin, answer)


print(answer)
