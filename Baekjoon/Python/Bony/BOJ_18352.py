import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cur_dist, cur_dest = heapq.heappop(queue)

        if distance[cur_dest] < cur_dist:
            continue

        for new_dest, new_dist in graph[cur_dest]:
            dist = cur_dist + new_dist

            if dist < distance[new_dest]:
                distance[new_dest] = dist
                heapq.heappush(queue, [dist, new_dest])


n, m, k, x = map(int, input().split())

INF = float('INF')
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
check = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))


dijkstra(x)

answer = []
for i in range(1, n+1):
    if distance[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i, end='\n')
