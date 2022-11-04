day = int(input())
cars = list(map(int, input().split()))
total = 0

for car in cars:
    if car == day:
        total += 1

print(total)
