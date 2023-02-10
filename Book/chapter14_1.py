n = int(input())
students = [input().split() for i in range(n)]

students.sort(
    key=lambda student: (-int(student[1]), int(student[2]), -int(student[3]), student[0]))

for student in students:
    print(student[0])
