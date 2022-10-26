import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[1])

p_list = []

for [p, d] in arr:
    heapq.heappush(p_list, p)
    if len(p_list) > d:
        heapq.heappop(p_list)

print(sum(p_list))
