boards = [[0 for _ in range(1001)] for _ in range(1001)]
n = int(input())

for i in range(1, n+1):
    x, y, w, h = map(int, input().split())

    for y in range(y, y+h):
        boards[y][x:(x+w)] = [i]*w

for i in range(1, n+1):
    result = 0

    for cnt in range(1001):
        result += boards[cnt].count(i)

    print(result)

print(boards)
