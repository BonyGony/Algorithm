
schoolNum = int(input())

answer = 0

for _ in range(schoolNum):
    studentNum, appleNum = map(int, input().split())

    answer += appleNum % studentNum

print(answer)
