def findCh(a, b, num):
    if num == 4:
        return [a, 0]
    elif num > 4:
        return [b, num-4]
    else:
        if num == 1:
            return [a, 3]
        elif num == 2:
            return [a, 2]
        else:
            return [a, 1]


def solution(survey, choices):
    answer = ''
    graphMap = {'R': 0,
                'T': 0,
                'C': 0,
                'F': 0,
                'J': 0,
                'M': 0,
                'A': 0,
                'N': 0,
                }

    for i in range(len(survey)):
        [a, b] = list(survey[i])
        [ch, num] = findCh(a, b, choices[i])
        graphMap[ch] += num

    graphList = list(graphMap.items())

    for i in range(0, len(graphList), 2):
        sortedLine = sorted(graphList[i:i+2], key=lambda x: x[1], reverse=True)
        answer += sortedLine[0][0]

    return answer


print(solution(["TR", "RT", "TR"],	[7, 1, 3]))
