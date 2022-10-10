def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    connect = set([costs[0][0]])

    while len(connect) != n:
        for [start, end, dis] in costs:
            if start in connect and end in connect:
                continue
            if start in connect or end in connect:
                connect.update([start, end])
                answer += dis
                break

    return answer
