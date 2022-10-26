def rangeCheck(nx, ny):
    if nx >= 0 and ny >= 0 and nx < n and ny < n:
        return True
    else:
        return False

def upDownDfs(x,y, depth):
    visitedUpDown[x][y] = 1;
    for i in range(2):
        nx = x + dxUpDown[i]
        ny = y + dyUpDown[i]
        if rangeCheck(nx, ny) and room[nx][ny] == 0  and visitedUpDown[nx][ny] != 1:
            return upDownDfs(nx, ny, depth+1)
    return depth

def leftRightDfs(x,y, depth):
    visitedLeftRight[x][y] = 1;
    for i in range(2):
        nx = x + dxLeftRight[i]
        ny = y + dyLeftRight[i]
        if rangeCheck(nx, ny) and room[nx][ny] == 0  and visitedLeftRight[nx][ny] != 1:
            return leftRightDfs(nx, ny, depth+1)
    return depth


n = int(input())

room = [[0]*n for _ in range(n)]
visitedUpDown = [[0]*n for _ in range(n)]
visitedLeftRight = [[0]*n for _ in range(n)]
dxUpDown = [-1,1]
dyUpDown = [0,0]
dxLeftRight = [0,0]
dyLeftRight = [-1,1]
leftRightCnt = 0
upDownCnt = 0

for i in range(n):
    line = list(input())
    for j in range(len(line)):
        if line[j] == 'X':
            room[i][j] = 1

for i in range(n):
    for j in range(n):
        if room[i][j] == 0 and visitedUpDown[i][j] != 1:
            L = upDownDfs(i, j, 1)
            if L >= 2:
                upDownCnt += 1
                
for i in range(n):
    for j in range(n):
        if room[i][j] == 0 and visitedLeftRight[i][j] != 1:
            L = leftRightDfs(i, j, 1)
            if L >= 2:
                leftRightCnt += 1

print(str(leftRightCnt) +" "+ str(upDownCnt))

