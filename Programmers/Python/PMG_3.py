import heapq


def solution(operations):
    answer = []
    heap = []

    for operation in operations:
        if operation[0] == "I":
            heapq.heappush(heap, int(operation[2:]))
        else:
            if len(heap) == 0:
                continue
            elif operation[2] == "-":
                heapq.heappop(heap)
            else:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)

    return answer


print(solution(["I -45", "I 653", "D 1", "I -642",
      "I 45", "I 97", "D 1", "D -1", "I 333"]))
