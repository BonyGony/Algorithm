n = int(input())
nArr = list(map(int, input().split()))

answer = 0


def dfs(arr):
    global answer

    if len(arr) == n:
        total = 0
        for j in range(n-1):
            total += abs(arr[j] - arr[j+1])
        answer = max(answer, total)
        return

    for num in nArr:
        if num not in arr:
            arr.append(num)
            dfs(arr)
            arr.pop()


dfs([])

print(answer)
