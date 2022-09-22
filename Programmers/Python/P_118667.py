from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    limit = (len(queue1) + len(queue2))*2

    if (sum1 + sum2) % 2 != 0:
        return -1

    while answer < limit:

        if sum1 == sum2:
            break
        elif sum1 > sum2:
            q1 = queue1.popleft()
            queue2.append(q1)
            sum2 += q1
            sum1 -= q1
        else:
            q2 = queue2.popleft()
            queue1.append(q2)
            sum2 -= q2
            sum1 += q2

        answer += 1

    if answer == limit:
        return -1

    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
