import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

input = sys.stdin.readline
n, m = map(int, input().split())
a, b, d = map(int, input().split())
islandArr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

visited[a][b] = 1
cnt += 1


def rangeCheck(x, y):
    if 0 <= x < n and 0 <= y <= m:
        return True
    else:
        return False


while 1:
    breakPoint = 0

    for _ in range(4):
        d = (d+3) % 4
        nextX = a + dx[d]
        nextY = b + dy[d]

        if rangeCheck(nextX, nextY) and islandArr[nextX][nextY] == 0:
            if visited[nextX][nextY] == 0:
                visited[nextX][nextY] = 1
                a = nextX
                b = nextY
                breakPoint = 1
                cnt += 1
                break

    if breakPoint == 0:
        if islandArr[a-dx[d]][b-dy[d]] == 1:
            print(cnt)
            break
        else:
            a, b = a-dx[d], b-dy[d]
