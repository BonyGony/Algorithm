from copy import deepcopy
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

r,c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
Map = [[0]*(c+2) for _ in range(r+2)]

for i in range(1,r+1):
    for j in range(1, c+1):
        if arr[i-1][j-1] == 'X':
            Map[i][j] = 1

copyMap = deepcopy(Map)

def rangeCheck(x,y):
    if x>=0 and x<c+2 and y>=0 and y<r+2:
        return True
    else:
        return False
    
def checkSurvivedIland(y,x):
    check = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if rangeCheck(nx,ny) and Map[ny][nx] == 0:
            check+=1
            
    if check >=3:
        copyMap[y][x] = 0
    

for i in range(r+2):
    for j in range(c+2):
        if Map[i][j] == 1:
            checkSurvivedIland(i,j)
            

# 출력
row = []
col = []

dic = {0: ".", 1: "X"}

for i in range(r+2):
    for j in range(c+2):
        if copyMap[i][j] == 1:
            row.append(i)
            col.append(j)

if row:
    row_l = min(row)
    row_h = max(row)
    col_l = min(col)
    col_h = max(col)

    for i in range(row_l, row_h + 1):
        for j in range(col_l, col_h + 1):
            print(dic[copyMap[i][j]], end="")
        print()

else:
    print('X')