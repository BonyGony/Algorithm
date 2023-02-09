n = int(input())
arr = [int(input()) for i in range(n)]

arr.sort(reverse=True)

for i in arr:
    print(i, end=' ')
