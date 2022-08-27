mushrooms = [int(input()) for _ in range(10)]

answer = 0
for mushroom in mushrooms:
    if answer + mushroom > 100:
        if (answer + mushroom) - 100 == 100 - answer:
            answer += mushroom
        elif (answer + mushroom) - 100 < 100 - answer:
            answer += mushroom
        break

    answer += mushroom

print(answer)
