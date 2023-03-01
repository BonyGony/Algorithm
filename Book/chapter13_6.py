# 인구 이동
from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rangeCheck(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False


def bfs(nowX, nowY):
    queue = deque()
    queue.append((nowX, nowY))
    avgCheckArr = [(nowX, nowY)]
    visited[nowX][nowY] = 1
    total = countries[nowX][nowY]

    while queue:
        [x, y] = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if rangeCheck(nx, ny) and (l <= abs(countries[x][y]-countries[nx][ny]) <= r) and visited[nx][ny] != 1:
                visited[nx][ny] = 1
                avgCheckArr.append((nx, ny))
                total += countries[nx][ny]
                queue.append((nx, ny))

    avg = total//len(avgCheckArr)

    for x, y in avgCheckArr:
        countries[x][y] = avg

    return len(avgCheckArr)


cnt = 0

while 1:
    check = False
    visited = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0 and bfs(x, y) > 1:
                check = True
                # for c in countries:
                #     print(c)
                # for v in visited:
                #     print(v)
                # print()

    if check == False:
        break
    else:
        cnt += 1
    # print('cnt : ', cnt)
    # print('===================')

print(cnt)
