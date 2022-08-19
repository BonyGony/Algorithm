def floyidWashal():
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                relations[start][end] = min(
                    relations[start][end], relations[start][mid] + relations[mid][end])


n = int(input())

inf = float('INF')
relations = [[inf]*n for _ in range(n)]
people = []
candidates = []
m = 0

for i in range(n):
    relations[i][i] = 0

while 1:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break

    relations[a-1][b-1] = 1
    relations[b-1][a-1] = 1

floyidWashal()

for i in range(n):
    num = max(relations[i])
    people.append([num, i+1])

people.sort()
m = people[0][0]
candidates.append(str(people[0][1]))

for i in range(1, n):
    if people[i][0] <= m:
        candidates.append(str(people[i][1]))

print(str(m)+" "+str(len(candidates)))
print(' '.join(candidates))
