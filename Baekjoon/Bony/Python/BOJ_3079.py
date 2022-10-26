import sys
input = sys.stdin.readline

n, m = map(int, input().split())
judgingTable = [int(input()) for _ in range(n)]

answer = 0
start = 0
end = m*max(judgingTable)

while start <= end:
    mid = (start+end)//2
    people = 0

    for table in judgingTable:
        people += mid//table

    if people >= m:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)
