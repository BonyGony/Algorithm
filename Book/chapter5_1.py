dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

n, m = map(int, input().split())
frame = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]


# 음료수 얼려먹기

def rangeCheck(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


def bfs(x, y):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if rangeCheck(nx, ny) and visited[nx][ny] != 1 and frame[nx][ny] == 0:
            bfs(nx, ny)


for x in range(n):
    for y in range(m):
        if visited[x][y] != 1 and frame[x][y] == 0:
            cnt += 1
            bfs(x, y)

print(cnt)
