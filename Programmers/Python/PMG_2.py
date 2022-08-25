from math import ceil


def solution(n, stations, w):
    answer = 0
    distance = []

    distance.append(stations[0]-w-1)

    for i in range(1, len(stations)):
        distance.append((stations[i]-w-1) - (stations[i-1]+w))

    distance.append(n - (stations[-1]+w))

    for dis in distance:
        answer += ceil(dis/((w*2)+1))

    print(distance)
    return answer


print(solution(16,	[9],	2))
