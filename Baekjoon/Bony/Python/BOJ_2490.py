arrs = [list(map(int, input().split())) for _ in range(3)]

for arr in arrs:
    t = 0
    for n in arr:
        if n == 0:
            t += 1

    if t == 0:
        print('E')
    elif t == 1:
        print('A')
    elif t == 2:
        print('B')
    elif t == 3:
        print('C')
    elif t == 4:
        print('D')
