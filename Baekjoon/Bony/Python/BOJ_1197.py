import sys
input = sys.stdin.readline

connects = set()
answer = 0


def findParent(x):
    if parent[x] != x:
        parent[x] = findParent(parent[x])

    return parent[x]


def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
parent = [i for i in range(V+1)]

graph.sort(key=lambda x: x[2])

for [s, e, w] in graph:
    if findParent(s) != findParent(e):
        unionParent(s, e)
        answer += w

print(answer)
