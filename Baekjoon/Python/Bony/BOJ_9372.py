import sys
input = sys.stdin.readline

testCase = int(input())


for _ in range(testCase):
    countryNum, plainNum = map(int, input().split())
    visitedCountry = [0]*(countryNum+1)
    countryMap = [[] for _ in range(countryNum+1)]

    for _ in range(plainNum):
        start, end = map(int, input().split())

        countryMap[start].append(end)
        countryMap[end].append(start)

    def DFS(idx, cnt):
        visitedCountry[idx] = 1

        for i in countryMap[idx]:
            if visitedCountry[i] == 0:
                cnt = DFS(i, cnt+1)

        return cnt

    print(DFS(1, 0))
