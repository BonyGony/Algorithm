arr = [list(input()) for _ in range(8)]
answer = 0

for i in range(8):
    if i % 2 == 0:
        ch = 'W'
    else:
        ch = 'B'

    for j in range(8):
        if arr[i][j] == 'F' and ch == 'W':
            answer += 1

        if ch == 'W':
            ch = 'B'
        else:
            ch = 'W'

print(answer)
