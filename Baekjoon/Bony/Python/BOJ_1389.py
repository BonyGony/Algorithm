def excuteFloydWashall(): # 1389 케빈 베이컨의 6단계 법칙 실버 1 플로이드-워셜    
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                friendShip[start][end] = min(friendShip[start][end], friendShip[start][mid] + friendShip[mid][end])
                
def getMin():
    min, answer = inf, 0
    
    for i in range(n):
        iSum = sum(friendShip[i])
        
        if iSum < min:
            min = iSum
            answer = i+1
            
    return answer

def initialize():
    for i in range(n):
        friendShip.append([inf] * n)
        friendShip[i][i] = 0
        
    for line in inputs:
        s, e = map(int, line.split(" "))
        friendShip[s - 1][e - 1] = friendShip[e - 1][s - 1] = 1

inf = float('INF')
n, m = map(int, input().split())
inputs = [input() for _ in range(m)]

friendShip = []

initialize()
excuteFloydWashall()

print(getMin())


