from collections import deque

F, S, G, U, D = map(int, input().split())

visitFloor = [0 for _ in range(F+1)]


def BFS():
    queue = deque()
    cnt = 0

    queue.append(S)
    visitFloor[S] = 1

    if S == G:
        return cnt

    while queue:
        length = len(queue)
        cnt += 1

        for _ in range(length):
            now = queue.popleft()
            nextUp = now+U
            nextDown = now-D

            if nextUp == G or nextDown == G:
                return cnt
            else:
                if nextUp <= F and visitFloor[nextUp] == 0:
                    queue.append(nextUp)
                    visitFloor[nextUp] = 1
                if nextDown > 0 and visitFloor[nextDown] == 0:
                    queue.append(nextDown)
                    visitFloor[nextDown] = 1

    if visitFloor[G] == 0:
        return 'use the stairs'


print(BFS())
