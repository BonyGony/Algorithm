# 연구소
from copy import deepcopy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
cases = []
answer = []


def rangeCheck(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


def bfs():
    queue = []
    copyLab = deepcopy(lab)

    for i in range(n):
        for j in range(m):
            if copyLab[i][j] == 2:
                queue.append([i, j])

    while queue:
        x, y = queue.pop()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if rangeCheck(nx, ny) and copyLab[nx][ny] == 0:
                copyLab[nx][ny] = 2
                queue.append([nx, ny])

    cnt = 0
    for i in range(n):
        for j in range(m):
            if copyLab[i][j] == 0:
                cnt += 1

    return cnt


def make_wall(depth):
    if depth == 3:
        answer.append(bfs())
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(depth+1)
                lab[i][j] = 0


make_wall(0)

print(max(answer))
