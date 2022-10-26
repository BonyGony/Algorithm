def nextPermutation(arr):
    nextIndex = 0
    reverseIndex = -1

    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            reverseIndex = i

    if reverseIndex == -1:
        return ''.join(arr)

    for i in range(len(arr) - 1, -1, -1):
        if arr[reverseIndex] < arr[i]:
            nextIndex = i
            break

    arr[reverseIndex], arr[nextIndex] = arr[nextIndex], arr[reverseIndex]
    new_arr = arr[:reverseIndex+1] + sorted(arr[reverseIndex+1:])

    return ''.join(new_arr)


n = int(input())
arr = []

for _ in range(n):
    arr.append(list(input()))

for sArr in arr:
    print(nextPermutation(sArr))
