c, r = map(int, input().split(" "))
k = int(input())

arr = [[0]*(c+2) for _ in range(r+2)]
x, y = 1, 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
nowD = 0
now = 1

if c*r < k:
    print(0)
else:
    for i in range(1, r+1):
        for j in range(1, c+1):
            arr[i][j] = 1

    while now < k:
        arr[x][y] = 0

        if arr[x+dx[nowD]][y+dy[nowD]] == 0:
            nowD = (nowD+1) % 4

        x += dx[nowD]
        y += dy[nowD]

        now += 1

    print(y, x)

# 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0
# 0 0 1 1 1 1 0
# 0 0 1 1 1 1 0
# 0 0 1 1 1 1 0
# 0 0 1 1 1 1 0
# 0 0 1 1 1 1 0
# 0 0 0 0 0 0 0
