import heapq
import sys
inf = sys.maxsize


def dijkstra(start):
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        cur_dist, cur_dest = heapq.heappop(queue)

        if distances[cur_dest] < cur_dist:
            continue

        for new_dest, new_dist in graph[cur_dest]:
            dist = cur_dist + new_dist

            if dist < distances[new_dest]:
                distances[new_dest] = dist
                heapq.heappush(queue, [dist, new_dest])


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distances = [inf] * (n+1)

for _ in range(m):
    s, e, d = map(int, input().split())

    graph[s].append((e, d))
    graph[e].append((s, d))

dijkstra(1)

print(distances[n])
