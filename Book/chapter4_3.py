case = 0
moveX = [-2, -1, 1, 2, 2, 1, -1, -2]
moveY = [-1, -2, -2, -1, 1, 2, 2, 1]
directions = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}

sArr = list(input())
x = int(sArr[1])
y = directions[sArr[0]]


def rangeCheck(x, y):
    if 1 <= x <= 8 and 1 <= y <= 8:
        return True
    else:
        return False


for i in range(8):
    nextX = x + moveX[i]
    nextY = y + moveY[i]

    if rangeCheck(nextX, nextY):
        case += 1

print(case)
