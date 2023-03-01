import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
passage = [input().split() for _ in range(n)]
Teachers = []


def bfs():
    for t in Teachers:
        for i in range(4):
            [x, y] = t
            while 0 <= x < n and 0 <= y < n:
                if passage[x][y] == "O":
                    break

                if passage[x][y] == "S":
                    return False

                x += dx[i]
                y += dy[i]

    return True


answer = False


def make_wall(depth):
    global answer
    if depth == 3:
        if bfs():
            answer = True
            return
    else:
        for i in range(n):
            for j in range(n):
                if passage[i][j] == "X":
                    passage[i][j] = "O"
                    make_wall(depth+1)
                    passage[i][j] = "X"


for x in range(n):
    for y in range(n):
        if passage[x][y] == "T":
            Teachers.append([x, y])

make_wall(0)

if answer == True:
    print("YES")
else:
    print("NO")
