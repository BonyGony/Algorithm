findSet = set(['a', 'e', 'i', 'o', 'u'])

sArr = list(input())
answer = 0

# print(sArr)

for ch in sArr:
    if ch in findSet:
        answer += 1

print(answer)
