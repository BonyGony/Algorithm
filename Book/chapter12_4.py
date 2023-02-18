# lock의 3배의 길이를 가진 보드를 만들고 가운데 위치에 lock을 위치
def boardsInit(lock):
    for r in range(n):
        for c in range(n):
            boards[n+r][n+c] = lock[r][c]

# 90도 회전 함수


def rotateKey(key):
    return list(zip(*key[::-1]))

# 가운데 lock 위치만 모두 1인지 확인하는 함수


def checkBoards():
    for r in range(n, 2*n):
        for c in range(n, 2*n):
            if boards[r][c] != 1:
                return False
    return True

# 자물쇠와 열쇠를 맞춰보는 함수


def boardsMatch(key):
    # 열쇠를 90, 180, 270, 360도로 회전시키며 확인
    for _ in range(4):
        key = rotateKey(key)

        # 가운데 lock을 기준으로, key의 오른쪽 아래가 lock의 0,0에 닿는 시점부터 key의 왼쪽 상단이 lock의 n,n에 닿는 시점까지 검사
        for r in range(1, 2*n):
            for c in range(1, 2*n):

                for x in range(m):
                    for y in range(m):
                        boards[r+x][c+y] += key[x][y]

                if checkBoards():
                    return True

                for x in range(m):
                    for y in range(m):
                        boards[r + x][c + y] -= key[x][y]
    return False


def solution(key, lock):
    global boards
    global m
    global n
    m = len(key)
    n = len(lock)
    boards = [[0]*(n*3) for _ in range(n*3)]

    boardsInit(lock)

    return boardsMatch(key)


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
