N = int(input());
people = list(map(int, input().split(" ")))
wait = [0 for _ in range(N)]


for i in range(N):
    k = i+1
    more = people[i];
    cnt = 0
    for j in range(N):
        if cnt == more and wait[j] == 0:
            wait[j] = k
            break
        elif wait[j] == 0:
            cnt += 1

print(wait)