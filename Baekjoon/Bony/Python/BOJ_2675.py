n = int(input())

for _ in range(n):
    num, s = input().split()
    num = int(num)
    answer = []

    for ch in s:
        for _ in range(num):
            answer.append(ch)

    print(''.join(answer))
