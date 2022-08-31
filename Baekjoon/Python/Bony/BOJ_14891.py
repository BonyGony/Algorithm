from collections import deque


def rotateRight(gearNum, d):
    if gearNum > 4 or gears[gearNum - 1][2] == gears[gearNum][6]:
        return

    if gears[gearNum - 1][2] != gears[gearNum][6]:
        rotateRight(gearNum + 1, -d)
        gears[gearNum].rotate(d)


def rotateLeft(gearNum, d):
    if gearNum < 1 or gears[gearNum][2] == gears[gearNum + 1][6]:
        return

    if gears[gearNum][2] != gears[gearNum + 1][6]:
        rotateLeft(gearNum - 1, -d)
        gears[gearNum].rotate(d)


gears = {}
answer = 0

for i in range(1, 5):
    gears[i] = deque(map(int, input()))

for _ in range(int(input())):
    gearNum, d = map(int, input().split())

    rotateRight(gearNum + 1, -d)
    rotateLeft(gearNum - 1, -d)
    gears[gearNum].rotate(d)


for i in range(4):
    answer += gears[i + 1][0] * (2 ** i)

print(answer)
