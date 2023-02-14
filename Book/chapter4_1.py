direction = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0]
}

n = int(input())
planArr = list(input().split())
nowX = 1
nowY = 1


def rangeCheck(x, y):
    if 1 <= x <= n and 1 <= y <= n:
        return True
    else:
        return False


for plan in planArr:
    [planX, planY] = direction[plan]

    if rangeCheck(nowX+planX, nowY+planY):
        nowX += planX
        nowY += planY
    else:
        continue

print(nowX, nowY)
