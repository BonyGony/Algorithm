# 특정 거리의 도시 찾기
import heapq

n, m, k, x = map(int, input().split())
distance = {node: float('inf') for node in range(1, n+1)}
graph = {}

for i in range(1, n+1):
    graph[i] = {}

for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1


def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [start, distance[start]])

    while queue:
        cur_dest, cur_dist = heapq.heappop(queue)

        if distance[cur_dest] < cur_dist:
            continue

        for new_dest, new_dist in graph[cur_dest].items():
            next_dist = cur_dist + new_dist

            if next_dist < distance[new_dest]:
                distance[new_dest] = next_dist
                heapq.heappush(queue, [new_dest, next_dist])


dijkstra(x)

check = False

for i in range(1, n+1):
    if distance[i] == k:
        check = True
        print(i)

if check == False:
    print(-1)
