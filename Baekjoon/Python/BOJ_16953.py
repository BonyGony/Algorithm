a,b = map(int, input().split(" "))
min = 99999

def BFS(n, depth):
    global min
    if b <= n:
        if b==n and min > depth:
            min = depth
        return
    
    BFS(n*2, depth+1)
    BFS(n*10+1, depth+1)
    
BFS(a, 1)

if min == 99999:
    print(-1)
else:
    print(min)