n = int(input())
arr = []

for _ in range(n):
    name, day, month, year = input().split()

    arr.append([int(year), int(month), int(day), name])

arr.sort()

# print(arr)

print(arr[len(arr)-1][3])
print(arr[0][3])
