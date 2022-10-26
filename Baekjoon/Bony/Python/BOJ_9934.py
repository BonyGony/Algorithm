n=int(input())
arr = list(map(int, input().split(" ")))
tree = [[] for _ in range(n)]
index = 0

def findNode(depth):
    global index
    if depth == n:
        return
    findNode(depth+1)
    tree[depth].append(arr[index]);
    index+=1
    findNode(depth+1)
    

findNode(0)

for t in tree:
    print(*t)