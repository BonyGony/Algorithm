n = int(input())
m = int(input())
arr = []
friendShip = [[0]*n for _ in range(n)];
friendMap = {}
friendSet = set()

for i in range(n):
    friendMap[i+1] = []

for _ in range(m):
    s,e = map(int, input().split(" "))
    if s in friendMap:
        friendMap[s].append(e)
        friendMap[e].append(s)
    else:
        friendMap[s] = [e]
        friendMap[e] = [s]

for i in friendMap[1]:
    friendSet.add(i)
    for j in friendMap[i]:
        friendSet.add(j)

if 1 in friendSet:
    friendSet.remove(1)
print(len(friendSet))