def solution(N, stages):
    answer = []
    failArr = [0]*(N+1)
    people = len(stages)

    # 각 스테이지 별로 머물러 있는 사람들 저장
    for stage in stages:
        if stage > N:
            continue
        failArr[stage] += 1

    arr = []

    # 스테이지별 싪패율 계산
    for i in range(1, N+1):
        if people > 0:
            arr.append([i, failArr[i]/people])
            people -= failArr[i]
        # 남은 유저수가 없으면 0으로 나누는 경우 런타임 에러 뜸. 실패율 0으로 저장
        else:
            arr.append([i, 0])

    arr.sort(reverse=True, key=lambda person: person[1])

    for [stage, fail] in arr:
        answer.append(stage)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4]))
