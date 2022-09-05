from itertools import combinations

N = int(input())

answers = []

for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        answers.append(int("".join(map(str, comb))))

answers.sort()

try:
    print(answers[N])
except:
    print(-1)
