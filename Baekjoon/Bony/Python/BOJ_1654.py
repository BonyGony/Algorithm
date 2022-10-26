k, n = map(int, input().split(" "))
rans = [int(input()) for _ in range(k)]

start = 1
end = max(rans)
mid = (start+end)//2

while start <= end:
    mid = (start+end)//2
    cnt = 0
    
    for ran in rans:
        cnt += ran//mid
        
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
        
    
print(end)