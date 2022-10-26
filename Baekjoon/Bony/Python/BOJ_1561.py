import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t_list = list(map(int, input().split()))

if n < m:
    print(n)

else:
    left = 0
    right = max(t_list)*n
    t = 0

    while left <= right:
        mid = (left+right) // 2
        cnt = m

        for i in range(m):
            cnt += mid // t_list[i]

        if cnt >= n:
            t = mid
            right = mid - 1
        else:
            left = mid + 1

    cnt = m

    for i in range(m):
        cnt += (t-1) // t_list[i]

    print(t, cnt)
    for i in range(m):
        if t % t_list[i] == 0:
            cnt += 1
        if cnt == n:
            print(i + 1)
            break
