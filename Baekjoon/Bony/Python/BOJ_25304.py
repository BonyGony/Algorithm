import sys
input = sys.stdin.readline

limit = int(input())
n = int(input())
total = 0

for _ in range(n):
    [price, num] = list(map(int, input().split()))
    total += price*num

if limit == total:
    print('Yes')
else:
    print("No")
