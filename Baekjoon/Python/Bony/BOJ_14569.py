import sys
input = sys.stdin.readline

subjects = []
students = []

subjectNum = int(input())

for _ in range(subjectNum):
    subjects.append(list(map(int, input().split()))[1:])

studentNum = int(input())

for _ in range(studentNum):
    students.append(list(map(int, input().split()))[1:])

for i in range(studentNum):
    cnt = 0
    for j in range(subjectNum):
        checkSet = set(students[i])
        checkSet.update(subjects[j])
        if len(checkSet) == len(students[i]):
            cnt += 1

    print(cnt)
