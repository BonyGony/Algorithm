arr = [int(input()) for _ in range(5)]
arr.sort()
total = 0

for a in arr:
    total += a

print(int(total/len(arr)))
print(arr[2])
