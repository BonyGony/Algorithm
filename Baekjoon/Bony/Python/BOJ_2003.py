import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 1
cnt = 0

while right <= n and left <= n:
    total = sum(arr[left:right])

    if total == m:
        cnt += 1
        right += 1

    elif total < m:
        right += 1

    else:
        left += 1

print(cnt)
