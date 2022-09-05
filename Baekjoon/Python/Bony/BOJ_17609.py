def findS(s):
    left = 0
    right = len(s)-1
    count = 0

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if left < right - 1:
                temp = s[:right] + s[right + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            if left + 1 < right:
                temp = s[:left] + s[left + 1:]
                if temp[:] == temp[::-1]:
                    return 1

            return 2

    return count


n = int(input())

sArr = []

for _ in range(n):
    sArr.append(input())

for s in sArr:
    print(findS(s))
