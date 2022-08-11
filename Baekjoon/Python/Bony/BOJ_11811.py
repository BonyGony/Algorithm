n = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(n)]
answer = [0]*n
out = ""

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        answer[i] = max(answer[i], arr[i][j] | arr[i][j])
        
for i in range(n):
    out += str(answer[i])+" "
    
print(out)