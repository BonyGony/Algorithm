from collections import deque
import sys
input = sys.stdin.readline


def findDis(order):
    if order == 'D':
        return (dis+1) % 4
    else:
        if dis == 0:
            return 3
        else:
            return dis-1


def rangeCheck(nx, ny):
    if 0 <= nx < n and 0 <= ny < n:
        return True
    else:
        False


n = int(input())
k = int(input())

boards = [[0 for _ in range(n)] for _ in range(n)]
dirDict = {}
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dis = 0
snake = deque()
time = 1

snake.append([0, 0])
boards[0][0] = 1

for _ in range(k):
    a, b = map(int, input().split())
    boards[a-1][b-1] = 2

l = int(input())

for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c


while True:
    [x, y] = snake.pop()
    nx = x + dx[dis]
    ny = y + dy[dis]

    if not rangeCheck(nx, ny) or boards[nx][ny] == 1:
        break

    elif boards[nx][ny] == 2:
        snake.append([x, y])
        snake.append([nx, ny])
        boards[nx][ny] = 1

    elif boards[nx][ny] == 0:
        snake.append([x, y])
        snake.append([nx, ny])
        boards[nx][ny] = 1
        [tail_x, tail_y] = snake.popleft()
        boards[tail_x][tail_y] = 0

    else:
        break
    # print(snake, time, t)
    if time in dirDict:
        # print("turn")
        dis = findDis(dirDict[time])
        # print(dx[dis], dy[dis])
    time += 1


print(time)
