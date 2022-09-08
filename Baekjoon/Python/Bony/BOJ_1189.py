import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
loads = [[0]*c for _ in range(r)]
visited = [[0]*c for _ in range(r)]
cnt = 0

for i in range(r):
    line = list(input())
    for j in range(len(line)):
        if line[j] == 'T':
            visited[i][j] = 1


def rangeCheck(nx, ny):
    if 0 <= nx < r and 0 <= ny < c:
        return True
    else:
        return False


def dfs(x, y, dis):

    if x == 0 and y == c-1:
        if k == dis:
            return 1
        return 0

    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if rangeCheck(nx, ny) and dis <= k and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += dfs(nx, ny, dis+1)
            visited[nx][ny] = 0

    return cnt


visited[r-1][0] = 1
print(dfs(r-1, 0, 1))
