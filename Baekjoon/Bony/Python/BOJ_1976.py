import sys
input = sys.stdin.readline


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


n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            unionParent(i+1, j+1)

plan = list(map(int, input().split()))
check = 1

for i in range(1, m):
    if parent[plan[i]] != parent[plan[0]]:
        check = 0

if check == 1:
    print('YES')
else:
    print('NO')
