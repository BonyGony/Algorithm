from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

boards = [[0 for _ in range(n)] for _ in range(n)]
dirDict = {}
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dis = 0
snake = deque()
time = 1
tail = [0, 0]

# 뱀의 시작위치를 넣어주고 boards에 몸통 표시
snake.append([0, 0])
boards[0][0] = 1

# 사과의 위치 2로 표시
for _ in range(k):
    a, b = map(int, input().split())
    boards[a-1][b-1] = 2

l = int(input())

# 해당하는 시간에 회전 시키기 위해 딕셔너리에 기록
for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

# 방향 회전 함수


def findDis(order):
    # D일 경우에는 오른쪽 90도 회전해야 하므로 dis가 1 증가
    if order == 'D':
        return (dis+1) % 4
    else:
        # L일 경우에는 왼쪽 90도 회전해야 하므로 dis가 1 감소
        if dis == 0:
            return 3
        else:
            return dis-1

# 뱀이 보드를 벗어 나는지 체크하는 함수


def rangeCheck(nx, ny):
    if 0 <= nx < n and 0 <= ny < n:
        return True
    else:
        False


# 벽을 만나거나 몸을 만날때까지 반복
while True:
    # 현재 머리쪽 좌표를 빼서 x, y를 얻는다
    [x, y] = snake.pop()
    # 다음 목적지 좌표
    nx = x + dx[dis]
    ny = y + dy[dis]

    # 벽을 만나거나 몸을 만나면 종료
    if not rangeCheck(nx, ny) or boards[nx][ny] == 1:
        break
    # 사과가 있는 경우
    elif boards[nx][ny] == 2:
        # 사과가 있는 칸으로 이동.
        # 빼줬던 원래 위치를 다시 넣어주고 사과 좌표를 추가적으로 append해줌. 그리고 보드에 몸통 표시
        snake.append([x, y])
        snake.append([nx, ny])
        boards[nx][ny] = 1
    # 다음칸에 사과가 없는 경우
    else:
        # 빼줬던 원래 위치를 다시 넣어주고 사과 좌표를 추가적으로 append해줌. 그리고 보드에 방문 표시
        snake.append([x, y])
        snake.append([nx, ny])
        boards[nx][ny] = 1
        # 사과가 없으므로 길이는 유지해야 하므로 꼬리칸을 빼줌. 몸통이 그 부분에 없으므로 0으로 만들어 줌.
        [tail_x, tail_y] = snake.popleft()
        boards[tail_x][tail_y] = 0

    # 회전 시켜야 할 시간이면 dis를 변화 시킴
    if time in dirDict:
        dis = findDis(dirDict[time])
    # 시간은 계속 1초씩 증가
    time += 1

print(time)
