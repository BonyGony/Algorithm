import sys
from collections import deque
from typing import Container
input = sys.stdin.readline

n, k = map(int, input().split())
container = deque(list(map(int, input().split())))


# left = arr[:n]
# right = arr[n:]
# container = deque(left+right[::-1])
check = 0
lv = 0
robot = deque([False] * (2*n))


while check < k:
    if robot[n-1] == True:
        robot[n-1] = False

    # print('before', container)

    container.rotate(1)
    robot.rotate(1)

    for i in range(n-1, -1, -1):
        if robot[i] == True:
            if i == (n-1):
                robot[i] = False
                continue

            if robot[i+1] == False and container[i+1] >= 1:
                robot[i] = False
                robot[i+1] = True
                container[i+1] -= 1
                if container[i+1] == 0:
                    check += 1

    if container[0] > 0:
        robot[0] = True
        container[0] -= 1

        if container[0] == 0:
            check += 1

    # print('after', container)
    # print(robot)
    # print(check, lv)

    lv += 1

print(lv)
