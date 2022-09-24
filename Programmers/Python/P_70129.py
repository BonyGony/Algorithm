
def solution(x):
    answer = []

    cnt = 0
    zero = 0

    while True:
        if x == '1':
            break
        zero += x.count('0')
        x = x.replace('0', '')

        x = bin(len(x))[2:]

        cnt += 1

    answer = [cnt, zero]

    return answer


print(solution("110010101001"))
