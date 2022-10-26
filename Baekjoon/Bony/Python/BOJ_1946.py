import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    registers = sorted([list(map(int,input().rsplit())) for _ in range(n)])
    m = registers[0][1]
    cnt = 0
    
    for i in range(1,n):
        target = registers[i][1]
        m = min(m, target)
        if m < target:
            cnt += 1
            
    print(n-cnt)
    