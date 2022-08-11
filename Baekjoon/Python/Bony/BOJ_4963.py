import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

check = 0

def rangeCheck(x,y):
    if y>=0 and y < w and x>=0 and x < h:
        return True
    else:
        return False
    
def dfs(x, y):
    visited[x][y] = 1
    for i in range(8):
        if rangeCheck(x+dx[i], y+dy[i]) and visited[x+dx[i]][y+dy[i]] == 0 and ilands[x+dx[i]][y+dy[i]] == 1:
            dfs(x+dx[i], y+dy[i])

while check != 1:
    global visited, ilands, w, h
    w, h = map(int, input().split(" "))
    visited = [[0]*w for _ in range(h)]
    ilands = []
    cnt = 0
    
    if w == 0 and h == 0:
        break
    
    for i in range(h):
        ilands.append(list(map(int, input().split(" "))))
    
    for i in range(h):
        for j in range(w):
            if ilands[i][j] == 1 and visited[i][j] != 1:
                cnt += 1
                dfs(i,j)
    
    print(cnt)