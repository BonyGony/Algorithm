def minNum(arr):
    m = 0
    length = len(arr)

    for start in range(length-3):
        for mid in (start+1, length-2):
            for end in (mid+1, length-1):
                num = arr[start] + arr[mid] + arr[end]
                lastNumS = str(num)
                lastNum = int(lastNumS[len(lastNumS)-1])

                if m < lastNum:
                    m = lastNum
    return m


n = int(input())
inputs = [list(map(int, input().split(" "))) for _ in range(n)]

persons = []


for i in range(n):
    persons.append([minNum(inputs[i]), i+1])

persons.sort(reverse=True)

print(persons[0][1])
