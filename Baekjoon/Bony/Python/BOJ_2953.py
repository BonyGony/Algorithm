arr = [list(map(int, input().split())) for _ in range(5)]
winner = 0
total = 0


for i in range(len(arr)):
    t = 0
    for n in arr[i]:
        t += n

    if total < t:
        total = t
        winner = i+1

print(str(winner)+' '+str(total))
