n = int(input())
arr = [input() for _ in range(n)]
arrSet = set(arr)

sortedArr = sorted(list(arrSet))
sortedArr = sorted(sortedArr, key=len)

# print(sortedArr)
# print('출력')

for i in range(len(sortedArr)):
    print(sortedArr[i])
