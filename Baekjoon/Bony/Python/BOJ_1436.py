n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


answer = []
cnt = 0
lank = 1

for [w, h] in arr:
    lank = 1

    for [nw, nh] in arr:
        if nw > w and nh > h:
            lank += 1

    print(lank)
