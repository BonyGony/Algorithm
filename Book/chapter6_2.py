
n = int(input())

students = dict()

for i in range(n):
    name, score = input().split()
    students[name] = int(score)

sorted_students = sorted(students.items(), key=lambda student: student[1])

for student in sorted_students:
    print(student[0], end=' ')

# --------------------------------

# n = int(input())

# students = []

# for i in range(n):
#     name, score = input().split()
#     students.append((name, score))

# sorted_students = sorted(students, key=lambda student: student[1])

# for student in sorted_students:
#     print(student[0], end=' ')

# --------------------------------

# n = int(input())

# students = []

# for i in range(n):
#     name, score = input().split()
#     students.append([name, score])

# sorted_students = sorted(students, key=lambda student: student[1])

# for student in sorted_students:
#     print(student[0], end=' ')
