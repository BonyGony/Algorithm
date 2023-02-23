# 미로 탈출

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]


def rangeCheck(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


def bfs(x, y):
    queue = deque()
    cnt = 0

    visited[x][y] = 1
    queue.append([x, y])

    while queue:
        length = len(queue)
        cnt += 1

        for _ in range(length):
            [nowX, nowY] = queue.popleft()

            if nowX == (n-1) and nowY == (m-1):
                print(cnt)
                queue = []
                break

            for i in range(4):
                nx = nowX + dx[i]
                ny = nowY + dy[i]

                if rangeCheck(nx, ny) and visited[nx][ny] == 0 and miro[nx][ny] == 1:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])


bfs(0, 0)
