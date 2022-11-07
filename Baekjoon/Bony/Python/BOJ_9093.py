n = int(input())

for _ in range(n):
    sArr = list(input().split())
    nArr = []

    for s in sArr:
        nArr.append(s[::-1])

    print(' '.join(nArr))
