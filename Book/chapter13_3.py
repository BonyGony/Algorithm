# 경쟁적 전염
from collections import deque

n, k = map(int, input().split())
examiner = [list(map(int, input().split())) for _ in range(n)]
s, destX, destY = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rangeCheck(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False


def bfs():
    queue = deque()
    time = 0

    for virus in range(1, k+1):
        for i in range(n):
            for j in range(n):
                if examiner[i][j] == virus:
                    queue.append((i, j, virus))

    while time < s:
        length = len(queue)

        for _ in range(length):
            x, y, virus = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if rangeCheck(nx, ny) and examiner[nx][ny] == 0:
                    examiner[nx][ny] = virus
                    queue.append((nx, ny, virus))
        time += 1


bfs()

print(examiner[destX-1][destY-1])
