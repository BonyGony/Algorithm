import heapq


def solution(n, works):
    answer = 0
    q = []

    for work in works:
        heapq.heappush(q, -work)

    while n > 0 and q:
        w = -heapq.heappop(q)
        w -= 1

        if w != 0:
            heapq.heappush(q, -w)
        n -= 1

    for t in q:
        answer += t*t

    return answer
