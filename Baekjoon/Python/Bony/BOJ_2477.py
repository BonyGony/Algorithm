n = int(input())

width = []
height = []
wH = []
bigSquare, smallSuqare = 0, 0
bigHeight, bigWidth = 0, 0
smallWidth, smallHeight = 0, 0

for _ in range(6):
    d, length = map(int, input().split())

    if d == 3 or d == 4:
        height.append(length)
    else:
        width.append(length)

    wH.append(length)

bigHeight = max(height)
bigWidth = max(width)

for i in range(len(wH)):
    if wH[i] == bigHeight:
        if i == 0:
            smallWidth = abs(wH[1] - wH[len(wH)-1])
        else:
            smallWidth = abs(wH[i-1] - wH[(i+1) % 6])

    if wH[i] == bigWidth:
        if i == 0:
            smallHeight = abs(wH[len(wH)-1] - wH[1])
        else:
            smallHeight = abs(wH[i-1] - wH[(i+1) % 6])

bigSquare = bigHeight * bigWidth
smallSuqare = smallWidth * smallHeight

print((bigSquare-smallSuqare)*n)
