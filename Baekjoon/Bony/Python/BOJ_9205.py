from collections import deque


def BFS(n):
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()

        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            return 'happy'

        for i in range(n):
            if not visitGs[i]:
                nextX, nextY = gs[i]

                if abs(x - nextX) + abs(y - nextY) <= 1000:
                    queue.append([nextX, nextY])
                    visitGs[i] = 1

    return 'sad'


testCase = int(input())

for _ in range(testCase):
    n = int(input())
    start = []
    gs = []
    end = []
    visitGs = [0 for _ in range(n)]
    start = list(map(int, input().split()))
    for _ in range(n):
        gs.append(list(map(int, input().split())))
    end = list(map(int, input().split()))

    print(BFS(n))
