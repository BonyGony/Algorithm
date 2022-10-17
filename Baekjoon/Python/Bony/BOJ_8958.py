n = int(input())


for _ in range(n):
    arr = list(input())
    num = 0
    score = 0

    for a in arr:
        if a == 'O':
            score += 1
            num += score
        else:
            score = 0

    print(num)
