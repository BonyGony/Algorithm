N = int(input())
answer = list(input().split(" "))
test = list(input().split(" "))

answerMap = {}
cnt = 0;
cntAll = int((N*(N-1))/2)

for i in range(N):
    answerMap[answer[i]] = i
    
for i in range(N):
    for j in range(i+1,N):
        if answerMap[test[i]] < answerMap[test[j]]:
            cnt += 1

print(str(cnt)+"/"+str(cntAll))