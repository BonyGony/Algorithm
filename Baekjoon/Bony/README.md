# [2022.10.28]

## BOJ_1233 주사위

- 난이도
  - 브론즈2
- 유형
  - 브루트포스
- 풀이
  - 3중 for문을 통해 전부 처리하며 중복되는 값을 체크한다
  - 제일 많이 나온 인덱스 값을 출력한다

# [2022.10.27]

## BOJ_14697 방 배정하기

- 난이도
  - 브론즈2
- 유형
  - 브루트포스
- 풀이
  - 모든 경우를 다 확인해 준다

# [2022.10.26]

## BOJ_3052 나머지

- 난이도
  - 브론즈2
- 유형
  - 수학
- 풀이
  - HashSet을 이용하여 중복을 없애 '서로 다른 나머지'를 만들어 준다.

# [2022.10.25]

## BOJ_1181 단어 정렬

- 난이도
  - 실버5
- 유형
  - 문자열
- 풀이
  - 중복을 없애기 위해 set을 사용한다
  - sort를 사용해 오름차순 정렬을 먼저 해준다.
  - 오름차순 정렬을 바탕으로 key=len으로 다시한번 정렬시킨다.

# [2022.10.24]

## BOJ_1427 소트인사이드

- 난이도
  - 실버5
- 유형
  - 문자열
- 풀이
  - 나눠서 리스트로 만들어준다.
  - sort 해준다.

# [2022.10.23]

## BOJ_5635 생일

- 난이도
  - 실버5
- 유형
  - 문자열
- 풀이
  - 배열에 연도, 월, 일, 이름 순으로 넣어준다.
  - sort를 해주면 맨 앞은 나이가 제일 많은 사람이, 맨 뒤에는 나이가 가장 적은 사람이 정렬된다.

# [2022.10.22]

## BOJ_10987 모음의 개수

- 난이도
  - 브론즈3
- 유형
  - 문자열
- 풀이
  - 빠른 검색을 위해 set을 사용하여 모음을 미리 넣어준다.
  - in을 사용하여 모음이 있으면 answer을 증가시킨다.

# [2022.10.21]

## BOJ_5988 홀수일까 짝수일까

- 난이도
  - 브론즈3
- 유형
  - 문자열
- 풀이
  - %를 사용하여 0이 나오면 짝수 아니면 홀수를 출력한다.

# [2022.10.20]

## BOJ_1100 하얀 칸

- 난이도
  - 브론즈2
- 유형
  - 문자열
- 풀이

  ```
    for i in range(8):
      if i % 2 == 0:
          ch = 'W'
      else:
          ch = 'B'

      for j in range(8):
          if arr[i][j] == 'F' and ch == 'W':
              answer += 1

          if ch == 'W':
              ch = 'B'
          else:
              ch = 'W'
  ```

  - 열이 짝수이면 화이트 칸 이므로 ch에 W를 넣어준다.
  - 그 행의 시작은 ch이고 한칸 이동할 때마다 W, B을 바꿔준다.
  - 말이 있을 때, 그 칸이 화이트인지 체크하고 answer에 더해준다.

# [2022.10.19]

## BOJ_11720 숫자의 합

- 난이도
  - 브론즈4
- 유형
  - 문자열
- 풀이
  - int로 바꿔서 더해준다.

# [2022.10.18]

## BOJ_2675 문자열 반복

- 난이도
  - 브론즈2
- 유형
  - 문자열
- 풀이

  ```
    for ch in s:
        for _ in range(num):
            answer.append(ch)

    print(''.join(answer))
  ```

  - 문자 하나를 횟수만큼 배열에 넣는다
  - 출력은 join을 통해 문자열로 만들어서 출력한다.

# [2022.10.17]

## BOJ_8958 OX퀴즈

- 난이도
  - 브론즈2
- 유형
  - 문자열
- 풀이

  ```
    num = 0
    score = 0

    for a in arr:
        if a == 'O':
            score += 1
            num += score
        else:
            score = 0
  ```

  - O인 경우에 스코어를 하나씩 올려주면서 더해준다. X가 나오면 Score를 0부터 다시 시작한다.

# [2022.10.16]

## BOJ_1152 단어의 개수

- 난이도
  - 브론즈2
- 유형
  - 문자열
- 풀이
  - 공백으로 나누어 리스트에 저장하고 리스트의 길이를 출력한다.

# [2022.10.15]

## BOJ_2480 주사위 세개

- 난이도
  - 브론즈4
- 유형
  - 수학
- 풀이
  - if else 문으로 조건을 나눈다.

# [2022.10.14]

## BOJ_9663 n-queen

- 난이도
  - 골드5
- 유형
  - 백트래킹
- 풀이
  - 일차원 배열 만들어서 각 인덱스를 열로 보고 푼다.

# [2022.10.13]

## BOJ_1436 덩치

- 난이도
  - 실버5
- 유형
  - 브루트포스
- 풀이
  - 자기보다 큰 사람만 체크
  - 그 인원수만큼 lank를 증가시켜 출력

# [2022.10.12]

## P_64062 징검다리 건너기

- 난이도
  - LV3
- 유형
  - 이분탐색
- 풀이
  - 건너는 인원을 mid로 잡는다.
  - 각 돌멩이를 mid로 빼주면서 연속으로 K번 이상인지 체크

# [2022.10.11]

## BOJ_1561 놀이 공원

- 난이도
  - 골드2
- 유형
  - 이분탐색
- 풀이
  - 놀이기구 수보다 아이들의 수가 적으면 n출력
  - 이분 탐색을 통해 아이들을 모두 태울 수 있는 시간 t를 구함
  - t-1 시간까지 몇 명의 아이를 태울 수 있는지 탐색
  - 제일 마지막에 탑승하는 놀이기구릐 번호를 출력

## BOJ_2109 순회강연

- 난이도
  - 골드3
- 유형
  - 그리디
- 풀이
  - d를 기준으로 정렬한다.
  - arr에서 p와 d를 꺼내면서 heapq에 집어 넣은다.
  - heapq의 길이가 d보다크면 heapq에서 제일 작은 값을 빼준다.

## BOJ_7570 줄 세우기

- 난이도
  - 골드3
- 유형
  - 그리디
- 풀이
  - 위치 배열을 만들어 각 원소의 위치를 넣어준다
  - 뒤 원소와 비교해서 더 작으면 카운트를 증가시킨다.
  - max값은 움직일 필요가 없는 애들의 갯수이므로 전체 수에서 빼준다.

# [2022.10.10]

## P_12927 야근 지수

- 난이도
  - LV3
- 유형
  - heap
- 풀이
  - heapq를 max heap으로 만들어 주고 다 넣어준다.
  - 제일 큰값을 하나씩 빼서 1을 빼주고 다시 넣어준다.
  - 0이 된 수는 제거해준다.
  - n값만큼 for문이 돌거나 queue가 비었으면 종료한다.

## BOJ_2252 줄 세우기

- 난이도
  - 골드 3
- 유형
  - 위상정렬

## BOJ_1197 최소 스패닝 트리

- 난이도
  - 골드 4
- 유형
  - 크루스칼

# [2022.10.09]

## P_42861 섬 연결하기

- 난이도
  - LV3
- 유형
  - 크루스칼

# [2022.10.08]

## P_12927 야근 지수

- 난이도
  - LV3
- 유형
  - heap
- 풀이
  - heapq를 max heap으로 만들어 주고 다 넣어준다.
  - 제일 큰값을 하나씩 빼서 1을 빼주고 다시 넣어준다.
  - 0이 된 수는 제거해준다.
  - n값만큼 for문이 돌거나 queue가 비었으면 종료한다.

# [2022.10.05]

## BOJ_2839 설탕 배달

- 난이도
  - 실버4
- 유형
  - 그리디
- 풀이

  ```
  while n >= 0:
    if n % 5 == 0:
        answer += (n // 5)
        print(answer)
        break
    n -= 3
    answer += 1
  else:
    print(-1)
  ```

  - n이 5로 나누어 떨어질 때까지 3을 빼주고 answer에 1을 더해준다.
  - 값이 마이너스가 된다면 못 찾은거기 때문에 -1 출력

# [2022.10.01]

## BOJ_1049 기타줄

- 난이도
  - 실버4
- 유형
  - 그리디
- 풀이

  ```
    allMin = min(allLines)
    oneMin = min(lines)

    if allMin < 6*oneMin:
        answer += allMin*(n//6)
        n = n % 6

        if allMin > n*oneMin:
            answer += oneMin*n
        else:
            answer += allMin
    else:
        answer += oneMin*n
  ```

  - 묶음 별 최소값과 낱개 별 최소값을 구해준다.
  - 묶음이 더 싸면, n을 6으로 나눈 몫만큼 answer에 더해준다. 남은 개수만큼 낱개 값을 더해준다.
  - 묶음이 낱개로 남은 개수만큼 가격보다 싸면, 묶음을 하나 더 산다.
  - 묶음이 더 비싸면, 낱개로 전부 구입한다.

# [2022.09.30]

## BOJ_20055 컨베이어 벨트 위의 로봇

- 난이도
  - 골드5
- 유형
  - 시뮬레이션

## BOJ_1439 뒤집기

- 난이도
  - 실버5
- 유형
  - 그리디
- 풀이
  ```
    for i in range(1, len(s)):
      if s[i] != s[i-1]:
        answer += 1
    print(math.ceil(answer/2))
  ```
  - 중간에 다른 숫자만 바꿔주면 된다.
  - 앞뒤가 다르면 answer을 증가시켜준다.
  - 맨 마지막이 다를 수도 있기에 2로 나눈것을 올림해준다.

# [2022.09.29]

## BOJ_1000 A+B

- 난이도
  - 브론즈5
- 유형
  - 수학

# [2022.09.28]

## BOJ_14888 연산자 끼워넣기

- 난이도
  - 실버1
- 유형
  - 브루트포스
- 풀이
  - permutation 사용하면 시간초과
  - dfs를 사용해서 구한다.

# [2022.09.27]

## BOJ_14503 로봇 청소기

- 난이도
  - 골드5
- 유형
  - 구현
- 풀이

  ```
    visited[r][c] = 1
    cnt += 1
  ```

  - 맨 처음 있는 공간을 청소한다.

  ```
    while 1:
      flag = 0

      for _ in range(4):

          d = (d+3) % 4
          nx = r + dx[d]
          ny = c + dy[d]

          if rangeCheck(nx, ny) and graph[nx][ny] == 0:
              if visited[nx][ny] == 0:
                  visited[nx][ny] = 1
                  cnt += 1
                  r = nx
                  c = ny
                  flag = 1
                  break

      if flag == 0:
          if graph[r-dx[d]][c-dy[d]] == 1:
              print(cnt)
              break
          else:
              r, c = r-dx[d], c-dy[d]
  ```

  - 일단 4방향을 전부 돌려준다.
  - 범위를 안 넘고 빈공간이면서 청소를 하지 않았으면 들어간다.
  - flag를 1로 만들어 청소한 것을 표시한다.
  - 만약 4방향 모두 청소하지 못 했으면 flag는 0이고 마지막 if문으로 들어간다.
  - 뒤쪽이 벽이면 cnt를 출력하고 종료
  - 뒤쪽이 벽이 아니면 후진해준다.

## BOJ_13458 시험 감독

- 난이도
  - 브론즈2
- 유형
  - 구현
- 풀이
  ```
    num = people[i]
    num -= b
    answer += 1
  ```
  - 해당 공간의 인원을 총 감독자만큼 빼준다. 한명이므로 한번만.
  ```
    answer += math.ceil(num/c)
  ```
  - 나머지 인원을 부감독관이 담당할 수 있는 인원으로 나누어주고 올림해준다.

# [2022.09.26]

## BOJ_2870 수학 숙제

- 난이도
  - 실버4
- 유형
  - 문자열
- 풀이
  ```
    p = re.compile('\d+')
    numArr = list(map(int, p.findall(s)))
  ```
  - 모든 반복되는 숫자를 패턴화 함.
  - findall 함수를 사용하여 리스트로 받고 int화 함

# [2022.09.25]

## BOJ_1264 모음의 개수

- 난이도
  - 브론즈4
- 유형
  - 문자열

# [2022.09.24]

## P_70129 이진 변환 반복하기

- 난이도
  - LV2
- 유형
  - 구현

# [2022.09.22]

## P_118667 두 큐 합 같게 만들기

- 난이도
  - LV2
- 유형
  - 그리디
- 풀이

  ```
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
  ```

  - 합이 홀수면 -1
  - queue1이 더크면 하나를 빼주고 queue2에 넣는다. queue2가 더 크면 반대.
  - answer이 limit과 같으면 못 만드는 것이므로 -1

  ## P_118666 성격 유형 검사하기

- 난이도
  - LV1
- 유형
  - 구현
- 풀이
  - dic에 성격 전부 초기화 해주고, 입력값에 따라 각 성격에 점수를 더해준다.
  - dic을 list로 만들어 2개씩 slice해주고 sorted를 이용해서 내림차순으로 만들어 준다.
  - 각 list당 0번째 단어를 answer에 더해준다.

# [2022.09.21]

## BOJ_14889 스타트와 링크

- 난이도
  - 실버2
- 유형
  - dfs
- 풀이
  - dfs

# [2022.09.19]

## BOJ_15686 치킨 배달

- 난이도
  - 골드5
- 유형
  - 브루트포스
- 풀이
  - 조합을 이용해서 치킨집을 m개 뽑는다.
  - 각 집마다 뽑은 치킨집 거리를 구해 최소를 구한다
  - 조합에서 구하는 최소에 더해준다
  - answer과 비교하여 최소값을 넣어준다

## BOJ_10819 차이를 최대로

- 난이도
  - 실버2
- 유형
  - 브루트포스
- 풀이

  ```
    def dfs(arr):
      global answer

      if len(arr) == n:
          total = 0
          for j in range(n-1):
              total += abs(arr[j] - arr[j+1])
          answer = max(answer, total)
          return

      for num in nArr:
          if num not in arr:
              arr.append(num)
              dfs(arr)
              arr.pop()
  ```

  - list에 하나씩 추가해주면서 재귀로 호출한다. 이때 안에 안 들어가 있는 것만(visited 활용가능).
  - arr의 개수가 n이면 최대값을 구해준다.
  - 다른 방법으로는, from itertools import permutations을 통해서 모든 순열을 구해서 계산해준다.

# [2022.09.18]

## BOJ_1920 수 찾기

- 난이도
  - 실버4
- 유형
  - HashMap
- 풀이

  ```
    numMap = {}

    n = int(input())
    nArr = list(input().split())
    for i in range(n):
        numMap[nArr[i]] = 1

    m = int(input())
    mArr = list(input().split())
    for i in range(m):
        if mArr[i] in numMap:
            print(1)
        else:
            print(0)
  ```

  - map을 만들어 입력값을 넣어준다.
  - 있는지 검사한다. O(1)이 걸린다.
  - 이분 탐색보다 훨씬 빠르다.

# [2022.09.17]

## BOJ_2003 수들의 합 2

- 난이도
  - 실버4
- 유형
  - 투 포인터
- 풀이

  ```
    left = 0
    right = 1
    cnt = 0

    while right <= n and left <= n:
        total = sum(arr[left:right])

        if total == m:
            cnt += 1
            right += 1

        elif total < m:
            right += 1

        else:
            left += 1
  ```

  - 구간의 합 == m : 카운트 증가. 다음 수를 찾기위해 오른쪽 포이터 이동.
  - 구간의 합 < m : 오른쪽 포인터 이동. 합을 올려야 함.
  - 구간의 합 > m : 왼쪽 포인터 이동. 합을 줄여야 함.

## BOJ_2998 8진수

- 난이도
  - 브론즈2
- 유형
  - 구현
- 풀이
  ```
    while len(s) % 3 != 0:
      s = '0'+s
  ```
  - 3으로 나누어 떨어질때까지 0을 앞에 붙여줌. 8은 2진수로 1000이므로, 7까지를 표현할 수 있는 세자리로 만들어 줌.
  ```
    for i in range(0, len(s), 3):
      answer += rule[s[i:i+3]]
  ```
  - 세자리씩 끊어서 rule에 있는 3자리수를 8진수로 바꾸어 줌.

# [2022.09.16]

## BOJ_2671 잠수함식별

- 난이도
  - 골드5
- 유형
  - 정규표현식
- 풀이
  ```
    re.compile('(100+1+|01)+').fullmatch(input())
  ```
  - '+' : 앞 문자열 반복
  - '()' : 문자열 묶음
  - '|' : 왼쪽 혹은 오른쪽 혹은 둘다

## BOJ_11005 진법 변환 2

- 난이도
  - 브론즈1
- 유형
  - 구현
- 풀이

  ```
    temp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n, b = map(int, input().split())

    answer = ''

    while n != 0:
      answer += str(temp[n % b])
    n = n//b

    print(answer[::-1])
  ```

  - 362를 10진수 다시 바꾸어 준다고 가정. 362를 10으로 나누면 몫은 36이고 나머지가 2이다.
  - temp에서 2번째 숫자를 의미하므로 answer = '2'
  - 36을 다시 10으로 나누어 주면 몫은 3이고 나머지는 6이다.
  - temp에서 6번째 숫자를 의미하므로 answer = '26'
  - 3을 10으로 나누어주면 몫은 0이고 나머지는 3이다.
  - temp에서 3번째 숫자를 의미하므로 answer = '263'
  - n이 0이 되므로 반복문은 빠져나가고 answer을 뒤집어 준다.

# [2022.09.15]

## BOJ_3190 뱀

- 난이도
  - 골드4
- 유형
  - 구현
- 풀이

  ```
    boards = [[0 for _ in range(n)] for _ in range(n)]
    dirDict = {}
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dis = 0
    snake = deque()
    time = 1
  ```

  - 시간에 따라 방향을 알려주므로 map을 이용하여 저장하여 준다. 찾는데 O(1)의 시간밖에 걸리지 않으므로 찾는 시간은 신경쓰지 않는다.
  - dx, dy를 초기값 오르쪽 방향부터 지정해준다.
  - dis 현재 방향이고 L 혹은 D값이 들어오면 -1, +1을 해주어 바꾸어준다.
  - 뱀의 상태를 저장하기 위해 snake를 설정. boards에 한칸 늘리고 지우는데 n\*n시간씩 걸리므로 꼬리와 머리를 queue에 저장하여 찾는 시간을 줄여준다.

  ```
  while True:
    [x, y] = snake.pop()
    nx = x + dx[dis]
    ny = y + dy[dis]

    if not rangeCheck(nx, ny) or boards[nx][ny] == 1:
        break

    elif boards[nx][ny] == 2:
        snake.append([x, y])
        snake.append([nx, ny])
        boards[nx][ny] = 1

    elif boards[nx][ny] == 0:
        snake.append([x, y])
        snake.append([nx, ny])
        boards[nx][ny] = 1
        [tail_x, tail_y] = snake.popleft()
        boards[tail_x][tail_y] = 0

    else:
        break
    # print(snake, time, t)
    if time in dirDict:
        # print("turn")
        dis = findDis(dirDict[time])
        # print(dx[dis], dy[dis])
    time += 1
  ```

  - queue에서 head를 가져와 다음값을 찾아준다. 찾는 값이 몸을 밟거나 범위를 벗어나면 종료.
  - 다음칸이 사과이면 몸만 늘려주고 boards에 표시해준다.
  - 다음값이 빈칸이면 몸을 늘려주고 꼬리를 다음칸으로 이동시킨다.
  - 시간이 dirDic에 존재하면 해당 문자를 가져와서 dis값을 바꾸어준다.

# [2022.09.14]

## BOJ_2302 극장 좌석

- 난이도
  - 실버1
- 유형
  - DP
- 풀이

  ```
    for i in range(3, 41):
      sit.append(sit[i-2]+sit[i-1])
  ```

  | **1** | **2** | **3** | **4** |
  | :---: | :---: | :---: | :---: |
  |   1   |  12   |  123  | 1234  |
  |       |  21   |  213  | 2134  |
  |       |       |  132  | 1324  |
  |       |       |       | 1243  |
  |       |       |       | 2143  |

  - dp[i] = dp[i-1] + dp[i-2]

  ```
    pre = 0

    for i in range(0, m):
        ans = ans * sit[vip[i]-1-pre]
        pre = vip[i]

    ans = ans * sit[n-pre]
  ```

  - |1|2|3|<span style="color:red">4</span>|5|6|<span style="color:red">7</span>|8|9|
  - 4기준 왼쪽 3개에 해당하는 dp[3]
  - 4와 7사이 2개에 해당하는 dp[2]
  - 7이후의 2개에 해당하는 dp[2]
  - 동시에 일어나는 경우이기 때문에 dp[3]*dp[2]*dp[2]

# [2022.09.13]

## BOJ_10833 사과

- 난이도
  - 브론즈1
- 유형
  - 구현
- 풀이
  - 종이별로 숫자를 달리하여 배열에 적어주고 각 숫자를 세어준다.

# [2022.09.12]

## BOJ_10163 색종이

- 난이도
  - 브론즈3
- 유형
  - 수학
- 풀이
  - 나머지를 구함

# [2022.09.10]

## BOJ_18352 특정 거리의 도시 찾기

- 난이도
  - 실버2
- 유형
  - 다익스트라
- 풀이
  - 기본 다익스트라 적용

# [2022.09.09]

## BOJ_1976 여행 가자

- 난이도
  - 골드4
- 유형
  - 분리 집합
- 풀이

  ```
    def findParent(x):
      if parent[x] != x:
        parent[x] = findParent(parent[x])
      return parent[x]


    def unionParent(a, b):
      a = findParent(a)
      b = findParent(b)

      if a < b:
        parent[b] = a
      else:
        parent[a] = b
  ```

  - 분리집합의 필수 두 함수.

  ```
    for i in range(n):
      line = list(map(int, input().split()))
      for j in range(n):
        if line[j] == 1:
          unionParent(i+1, j+1)
  ```

  - 연결된 노드를 union 해준다.

  ```
    for i in range(1, m):
      if parent[plan[i]] != parent[plan[0]]:
        check = 0
  ```

  - 여행 계획 첫번째 도시의 parent와 비교해서 다르면 NO 맞으면 YES를 출력한다.

---

## BOJ_3039 입국심사

- 난이도
  - 골드5
- 유형
  - 이분탐색
- 풀이

  ```
    start = 0
    end = m*max(judgingTable)
  ```

  ```
    while start <= end:
      mid = (start+end)//2
      people = 0

      for table in judgingTable:
        people += mid//table

      if people >= m:
        end = mid - 1
        answer = mid
      else:
        start = mid + 1
  ```

  - mid를 중간값으로 잡아주고 그 중간값을 심사대로 나눠주어 people에 저장한다
  - people이 m보다 크면 end값을 줄여준다. 반대는 start값을 올려준다.

# [2022.09.08]

## BOJ_1189 컴백홈

- 난이도
  - 실버1
- 유형
  - dfs
- 풀이

  ```
    if x == 0 and y == c-1:
        if k == dis:
            return 1
        return 0
  ```

  - 조건 탈출문. 마지막 도착지점에서 k거리이면 1을 리턴

  ```
    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if rangeCheck(nx, ny) and dis <= k and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += dfs(nx, ny, dis+1)
            visited[nx][ny] = 0

    return cnt
  ```

  - 4방향에 대한 재귀를 돌려준다.
  - 거리가 k를 넘어가면 할 필요가 없고 방문한 곳은 피해준다.
  - 방문 체크를 하고 재귀를 넘겨주고 돌아오면 방문 체크를 풀어준다
  - cnt를 리턴해준다

# [2022.09.07]

## BOJ_4386 별자리 만들기

- 난이도
  - 골드4
- 유형
  - 크루스칼 알고리즘
- 풀이

  ```
    edges.append(
            (math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))
  ```

  - 기본적인 크루스칼 알고리즘을 적용한다.
  - edge 계산을 해주는게 포인트.

  ```
    for edge in edges:
      cost, x, y = edge

      if find_parent(x) != find_parent(y):
        union_parent(x, y)
        result += cost
  ```

  - 정렬된 edge를 작은순에서 큰순으로 받아온다.
  - root 노드가 같지않으면 순환구조가 아니므로 union 시켜준다

# [2022.09.06]

## BOJ_1461 도서관

- 난이도
  - 골드5
- 유형
  - 정렬
- 풀이

  ```
    if maxNum == plus[0]:
        plusIndex = m
        answer += plus[0]
    else:
        minusIndex = m
        answer += abs(minus[0])

    for i in range(plusIndex, len(plus), m):
        answer += plus[i]*2

    for i in range(minusIndex, len(minus), m):
        answer += abs(minus[i])*2
  ```

  - plus부분과 minus부분을 나누어 준다.
  - max값 있는 곳을 체크해주고 m만큼의 index값을 증가시켜준다. 그리고 max값을 더해준다.
  - 각 배열에서 m만큼씩 이동하면서 더해준다

## BOJ_14569 시간표 짜기

- 난이도
  - 실버2
- 유형
  - 구현
- 풀이

  ```
    checkSet = set(students[i])
    checkSet.update(subjects[j])
    if len(checkSet) == len(students[i]):
      cnt += 1
  ```

  - i번째 학생으로 set을 만들어주고 j번째 과목을 합쳐준다.
  - 학생 스케쥴에 변화가 없으면 시간표가 일치 함으로 cnt를 올려준다.

# [2022.09.05]

## BOJ_11497 통나무 건너뛰기

- 난이도
  - 실버1
- 유형
  - 정렬
- 풀이

  ```
    logs.sort()
    upDownArr = logs[0:n-1:2] + logs[-1::-2]
  ```

  - 통나무들을 정렬해서 중간을 최대값으로 두고 증가 감소 형태로 만들어준다

# [2022.09.03]

## BOJ_2156 포도주 시식

- 난이도
  - 실버1
- 유형
  - dp
- 풀이

  ```
    dp[i] = max(dp[i-3]+wines[i]+wines[i-1], dp[i-2]+wines[i], dp[i-1])
  ```

  - 두번째 전에 것을 안 먹었을 때 : dp[i-3]+wines[i]+wines[i-1]
  - 첫번째 전에 것을 안 먹었을 때 : dp[i-2]+wines[i]
  - 지금 것을 안 먹었을 때 : dp[i-1]
  - 위 세가지 경우 중 가장 큰 것을 찾는다.

---

## BOJ_5052 전화번호 목록

- 난이도
  - 골드4
- 유형
  - 정렬
- 풀이

  ```
    numArr.sort()
  ```

  - 정렬을하면 앞뒤만 비교해도 된다. 모든 경우 찾으려 하면 시간초과.

  ```
    def prefixCheck():
    for i in range(1, len(numArr)):
        if numArr[i-1] == numArr[i][0:len(numArr[i-1])]:
            return 'NO'

    return 'YES'
  ```

  - 앞뒤 비교해서 prefix로 존재하면 no 리턴하고 아니면 yes 리턴.

# [2022.09.02]

## BOJ_5430 AC

- 난이도
  - 골드5
- 유형
  - 구현
- 풀이

  ```
    numArr = deque(input()[1:-1].split(','))
  ```

  - 문자열 파싱하는 것이 포인트

  ```
    reverse = 0

    if order == 'R':
      reverse += 1
  ```

  - R이 들어올때마다 reverse를 해주면 시간초과...
  - 짝수번이면 해줄필요 없다

  ```
    elif order == 'D':
      if len(numArr) == 0:
          raise

      if reverse % 2 == 0:
          numArr.popleft()
      else:
          numArr.pop()
  ```

  - 다만 거기에 맞춰서 짝수번이면 왼쪽 삭제
  - 홀수번이면 오른쪽 삭제해준다

  - 모든 조합을 구해서 answer에 넣어준다

# [2022.09.01]

## BOJ_1038 감소하는 수

- 난이도
  - 골드5
- 유형
  - 브루트포스
- 풀이

  ```
    answers = []

    for i in range(1, 11):
      for comb in combinations(range(0, 10), i):
          comb = list(comb)
          comb.sort(reverse=True)
          answers.append(int("".join(map(str, comb))))

      answers.sort()
  ```

  - 모든 조합을 구해서 answer에 넣어준다

---

## BOJ_9205 맥주 마시면서 걸어가기

- 난이도
  - 실버1
- 유형
  - BFS
- 풀이

  ```
    def BFS(n):
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()

        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            return 'happy'

        for i in range(n):
            if not visitGs[i]:
                nextX, nextY = gs[i]

                if abs(x - nextX) + abs(y - nextY) <= 1000:
                    queue.append([nextX, nextY])
                    visitGs[i] = 1

    return 'sad'
  ```

  - 가까운 편의점부터 거리가 1000 이하이면 집어 넣는다.
  - 종료문으로 패스티벌 까지의 거리가 1000 이하이면 happy
  - 패스티벌까지 못가면 sad

# [2022.08.31]

## BOJ_5014 스타트링크

- 난이도
  - 골드5
- 유형
  - BFS
- 풀이
  - deque를 사용한 BFS를 사용한다

# [2022.08.30]

## BOJ_14891 톱니바퀴

- 난이도
  - 골드5
- 유형
  - 구현
- 풀이
  - 기준 톱니 오른쪽으로 재귀로 돌려준다
  - 그 뒤, 왼쪽으로 재귀로 돌려준다

# [2022.08.29]

## BOJ_17609 회문

- 난이도
  - 골드5
- 유형
  - 투포인터
- 풀이
  - 각 끝에서부터 비교해준다

# [2022.08.27]

## BOJ_9372 상근이의 여행

- 난이도
  - 실버5
- 유형
  - DFS
- 풀이

```
def DFS(idx, cnt):
        visitedCountry[idx] = 1

        for i in countryMap[idx]:
            if visitedCountry[i] == 0:
                cnt = DFS(i, cnt+1)

        return cnt
```

- visit 체크를 하면서 DFS로 쭉 돌아준다

# [2022.08.25]

## BOJ_2851 슈퍼마리오

- 난이도
  - 브론즈1
- 유형
  - 구현
- 풀이

```
for mushroom in mushrooms:
    if answer + mushroom > 100:
        if (answer + mushroom) - 100 == 100 - answer:
            answer += mushroom
        elif (answer + mushroom) - 100 < 100 - answer:
            answer += mushroom
        break

    answer += mushroom
```

- 100을 기준으로 비교해서 더해준다

# [2022.08.23]

## P 등굣길

- 난이도
  - LV3
- 유형
  - dp
- 풀이

```
dp[i][j] = (dp[i-1][j] + dp[i][j-1])
```

## P 이중우선순위큐

- 난이도
  - LV3
- 유형
  - heap
- 풀이
  - 기지국 사이의 빈 아파트 길이를 각각 구해준다
  - 각각의 거리를 (w\*2+1)로 나누어 주고 올림해서 answer에 더해준다

# [2022.08.22]

## P 기지국 설치

- 난이도
  - LV3
- 유형
  - 구현
- 새로 알게된 내용
  - 파이썬의 heapq에서 nlargest(n, iterable)라는 함수가 있다. 이걸로 최대값을 찾을 수 있다.
  - heapq.heapify로 최소힙으로 다시 정렬 가능.
- 풀이
  ```
  elif operation[2] == "-":
    heapq.heappop(heap)
  else:
    heap = heapq.nlargest(len(heap), heap)[1:]
    heapq.heapify(heap)
  ```
  - '-'일때 최소값을 빼주고, 최대값을 빼줄 때에는 nlargest를 이용해서 최대값인 첫번째 인자를 제외하고 배열을 만든다.
  - 만든 배열을 heapify를 통해 최소힙으로 다시 만들어 준다.

# [2022.08.21]

## P 입국심사

- 난이도
  - LV3
- 유형
  - 이분탐색
- 풀이

  ```
    start = 0
    end = max(times) * n

    while start <= end:
        mid = (start+end)//2
        people = 0

        for time in times:
            people += mid//time

            if people >= n:
                break

        if people >= n:
            answer = mid
            end = mid - 1
        elif people < n:
            start = mid + 1
  ```

  - 같은 시간동안 각각이 처리한는 수가 다르므로 ran선 자르기와 비슷함.
  - end 범위를 가장 오래걸리는 심사대 \* n 을 해주어 설정해 줌.
  - poeple에 같은 시간동안 각 심사대에서 처리해 준 인원을 넣어준다
  - n보다 크면 시간이 많다는 뜻으로 end값을 줄여준다. 작다면 start값을 올려준다.

---

# [2022.08.19]

## BOJ_2660 회장뽑기

- 난이도
  - 골드 5
- 유형
  - 플로이드-와샬
- 풀이
  - 플로이드-와샬
  - 각 노드별 max값
  - 그 중 제일 작은 값 기준으로 후보자 뽑음

---

## BOJ_2477 참외밭

- 난이도
  - 실버 3
- 유형
  - 구현
- 풀이
  - 가로 제일 큰 값 기준 : |좌 - 우| => 작은 사각형 세로
  - 세로 제일 큰 값 기준 : |좌 - 우| => 작은 사각형 가로
  - 큰 사각형 - 작은 사각형

---

# [2022.08.18]

## BOJ_5972 택배 배송

- 난이도
  - 골드 5
- 유형
  - 다익스트라
- 풀이
  - 기본 다익스트라 구현해서 적용

---

## BOJ_14584 암호 해독

- 난이도
  - 실버 5
- 유형
  - 브루트포스
- 풀이

```
   def changeNextS(s):
    sArr = list(s)

    for i in range(len(sArr)):
        chrNum = ord(sArr[i])
        if chrNum + 1 > 122:
            sArr[i] = chr(chrNum+1-26)
        else:
            sArr[i] = chr(chrNum+1)

    return ''.join(sArr)
```

- 하나씩 뒤로 바꾸면서 단어가 있는지 체크한다.

---

# [2022.08.17]

## BOJ_10157 자리배정

- 난이도
  - 실버 4
- 유형
  - 구현
- 풀이

```
   0 0 0 0 0 0 0
   0 1 1 1 1 1 0
   0 1 1 1 1 1 0
   0 1 1 1 1 1 0
   0 1 1 1 1 1 0
   0 1 1 1 1 1 0
   0 1 1 1 1 1 0
   0 0 0 0 0 0 0
```

- (1,1)부터 0으로 만들어 주면서 이동한다. 다음이 0이면 방향을 돌려준다.

---

## BOJ_2303 숫자 게임

- 난이도
  - 실버 5
- 유형
  - 브루트포스
- 풀이

  ```
  for start in range(length-3):
        for mid in (start+1, length-2):
            for end in (mid+1, length-1):
                num = arr[start] + arr[mid] + arr[end]
                lastNumS = str(num)
                lastNum = int(lastNumS[len(lastNumS)-1])

                if m < lastNum:
                    m = lastNum
  ```

  - 모든 경우를 탐색해서 최대값을 찾아준다

---

# [2022.08.16]

## BOJ_9081 단어 맞추기

- 난이도
  - 실버 1
- 유형
  - 구현
- 풀이
  - 뒤쪽부터 오름차순인지 검사
  - 전부 오름차순이면 끝단어. 아니면 내림차순으로 바뀌는 부분을 체크
  - 체크한 알파벳보다 큰 알파벳을 뒤쪽부터 검사해서 체크
  - 두 체크한 부분을 swap 하고 첫번째 체크 부분 이후를 정렬해서 붙여줌.

---

## BOJ_1652 누울 자리를 찾아라

- 난이도
  - 브론즈 1
- 유형
  - DFS
- 풀이

  ```
  def upDownDfs(x,y, depth):
    visitedUpDown[x][y] = 1;
    for i in range(2):
        nx = x + dxUpDown[i]
        ny = y + dyUpDown[i]
        if rangeCheck(nx, ny) and room[nx][ny] == 0  and visitedUpDown[nx][ny] != 1:
            return upDownDfs(nx, ny, depth+1)
    return depth
  ```

  - DFS를 이용해서 depth가 2 이상인 경우를 찾아준다. 위의 코드는 세로 확인이고 비슷하게 가로 검사도 만들어서 진행한다

---

# [2022.08.15]

## BOJ_7490 0 만들기

- 난이도
  - 골드 5
- 유형
  - 브루트포스
- 새로 알게된 내용
  - eval()
    - 문자열을 계산할 수 있음
- 풀이

  ```
  def makeZero(arr, n):

    ar = deepcopy(arr)
    ar.append(str(n))

    if len(ar) == (N+N-1):
        s = ''.join(ar).replace(" ", "")
        if eval(s) == 0:
            answer.append(''.join(ar))
        return

    ar.append(' ')
    makeZero(ar, n+1)
    ar.pop()

    ar.append('+')
    makeZero(ar, n+1)
    ar.pop()

    ar.append('-')
    makeZero(ar, n+1)
    ar.pop()
  ```

  - 재귀를 이용해서 모든 경우를 탐색한다

---

# [2022.08.14]

## BOJ_1654 랜선 자르기

- 난이도
  - 실버2
- 유형
  - 이분탐색
- 풀이

  ```
  while start <= end:
    mid = (start+end)//2
    cnt = 0

    for ran in rans:
        cnt += ran//mid

    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
  ```

  - 이분탐색을 이용한다

---

# [2022.08.13]

## BOJ_11000 강의실 배정

- 난이도
  - 골드 5
- 유형
  - 우선순위 큐
- 풀이

  ```
  for i in range(1, N):
    if rooms[i][0] < queue[0]:
        heapq.heappush(queue, rooms[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, rooms[i][1])
  ```

---

# [2022.08.12]

## BOJ_15729 방탈출

- 난이도
  - 실버 2
- 유형
  - 그리디
- 풀이

  ```
  for i in range(n):
        if targetButtons[i] != startButtons[i]:
            cnt += 1
            clickButton(i)
  ```

  - 두개를 비교해서 다르면 눌러준다

---

## BOJ_15787 기차가 어둠을 해치고 은하수를

- 난이도
  - 실버 2
- 유형
  - 구현
- 풀이

  ```
  def commandOrder(orderNum, trainNum, seatNum = 1 ):
    if orderNum == 1:
        trains[trainNum][seatNum] = 1
    elif orderNum == 2:
        trains[trainNum][seatNum] = 0
    elif orderNum == 3:
        trains[trainNum].rotate(1)
        trains[trainNum][0] = 0
    elif orderNum == 4:
        trains[trainNum].rotate(-1)
        trains[trainNum][19] = 0
  ```

  - deque 이용하여 해결

---

# [2022.08.11]

## BOJ_1389 케빈 베이컨의 6단계 법칙

- 난이도
  - 실버 1
- 유형
  - 플로이드-워셜
- 풀이

  ```
  def excuteFloydWashall():
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                friendShip[start][end] = min(friendShip[start][end], friendShip[start][mid] + friendShip[mid][end])

  for i in range(n):
        iSum = sum(friendShip[i])

        if iSum < min:
            min = iSum
            answer = i+1
  ```

  - 플로이드-워셜로 각 노드의 end point까지의 거리를 구하고 노드 list의 총합을 비교해 답을 찾는다

---

## BOJ_1759 암호 만들기

- 난이도
  - 골드 5
- 유형
  - 브루트포스, dfs
- 풀이

  ```
  def dfs(s, depth, i):
    if depth == n and findCollection(s):
        print(s)

    for c in range(i, len(inputs)):
        dfs(s+inputs[c], depth+1, c+1)
  ```

  - dfs로 검사해준다.

---

## BOJ_16953 A -> B

- 난이도
  - 실버 2
- 유형
  - BFS
- 풀이

  ```
  def BFS(n, depth):
    global min
    if b <= n:
        if b==n and min > depth:
            min = depth
        return

    BFS(n*2, depth+1)
    BFS(n*10+1, depth+1)
  ```

a\*2한 값이랑 뒤에 1을 추가해 준 값이랑 둘다 찾는다

---

# [2022.08.10]

## BOJ_11811 데스스타

- 난이도
  - 실버 3
- 유형
  - 비스마스킹
- 풀이

  ```
  answer[i] = max(answer[i], arr[i][j] | arr[i][j])
  ```

  and연산의 결과 이기에 or 연산으로도 값을 얻을 수 있음

---

## BOJ_1720 타일 코드

- 난이도
  - 골드 4
- 유형
  - DP
- 풀이

  ```
  dp[i] = dp[i-1] + dp[i-2] * 2
  ```

  - 2\*1 한개 사용 경우 + (n-1까지의 경우)
  - 2\*1 두개 사용 경우 + (n-2까지의 경우)
  - 2\*2 두개 사용 경우 + (n-2까지의 경우)
  - => dp[n] = dp[n-1] + 2\*dp[n-2]
  - => 여기서 좌우 대칭을 없애줘야 함
  - => dp[n]/2는 자기자신이 좌우대칭이 경우까지 중복해서 없애주는 경우가 발생
  - => (dp[n] - 자기자신대칭)/2 + 자기자신대칭

  ```
  if n % 2 == 0:
    dp[n] - (2*dp[(n-2)//2] + dp[n//2]))//2 + (2*dp[(n-2)//2] + dp[n//2]
  ```

  - 짝수인 경우
    - n/2 + (중간 없음) + n/2
    - (n-2)/2 + (1\*2타일 두개) + (n-2)/2
    - (n-2)/2 + (2\*2타일 한개) + (n-2)/2
    - 위 세개의 case만 따로 빼준다
    - => 2\*dp[(n-2)//2] + dp[n//2]

  ```
  else:
    (dp[n] - dp[(n-1)//2])//2 + dp[(n-1)//2]
  ```

  - 홀수인 경우
    - (n-1)/2 + (중간 한개) + (n-1)/2
    - => dp[(n-1)//2]

---

# [2022.08.09]

## BOJ_5212 지구 온난화

- 난이도
  - 실버 2
- 유형
  - 구현
- 풀이

  ```
  def checkSurvivedIland(y,x):
    check = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if rangeCheck(nx,ny) and Map[ny][nx] == 0:
            check+=1

    if check >=3:
        copyMap[y][x] = 0
  ```

  Map에서 3면이 바다인지 체크해서 copyMap을 바꿔줌.

---

## BOJ_1946 신입 사원

- 난이도
  - 실버 2
- 유형
  - 정렬, 그리디
- 풀이

  ```
  for i in range(1,n):
        target = registers[i][1]
        m = min(m, target)
        if m < target:
            cnt += 1
  ```

  면접 점수로 sort 해주고 시작하면 나머지 하나 점수만 비교하면 됨.

---

## BOJ_4963 섬의 개수

- 난이도
  - 실버 2
- 유형
  - DFS, BFS
- 풀이

  ```
  def dfs(x, y):
    visited[x][y] = 1
    for i in range(8):
        if rangeCheck(x+dx[i], y+dy[i]) and visited[x+dx[i]][y+dy[i]] == 0 and ilands[x+dx[i]][y+dy[i]] == 1:
            dfs(x+dx[i], y+dy[i])
  ```

  dfs로 해당 경로 전부 찾고 visited가 0일 때만 접근.

---

# [2022.08.08]

## BOJ_1406 에디터

- 난이도
  - 실버 2
- 유형
  - 스택
- 풀이

  ```
  if order[0] == "P":
        left.append(order[2])
  elif order[0] == "L" and left != []:
        right.append(left.pop())
  elif order[0] == "D" and right != []:
        left.append(right.pop())
  elif order[0] == "B" and left != []:
        left.pop()
  ```

  left|cursor|right

---

## BOJ_9934 완전 이진 트리

- 난이도
  - 실버 1
- 유형
  - 트리, 재귀
- 풀이

  ```
  def findNode(depth):
    global index
    if depth == n:
        return
    findNode(depth+1)
    tree[depth].append(arr[index]);
    index+=1
    findNode(depth+1)
  ```

  중위 순회 방식 재귀

---

## BOJ_9375 패션왕 신해빈

- 난이도
  - 실버 3
- 유형
  - 조합론, map
- 풀이

  ```
  for v in clothesDic.values():
        result *= (v+1)
  result -= 1
  ```

  (1번 종류 개수 + 1)_(2번 종류 개수 + 1) _ ... - 1 = 답

---

# [2022.08.07]

## BOJ_5567 결혼식

- 난이도
  - 실버 2
- 유형
  - 그래프탐색
- 풀이

  ```
  for _ in range(m):
    s,e = map(int, input().split(" "))
    if s in friendMap:
        friendMap[s].append(e)
        friendMap[e].append(s)
    else:
        friendMap[s] = [e]
        friendMap[e] = [s]

    for i in friendMap[1]:
        friendSet.add(i)
        for j in friendMap[i]:
            friendSet.add(j)
  ```

  양 방향 그래프 설정을 해준 뒤, 1친구들, 그 다음친구들까지 찾아서 set에 추가해 준다.

---

## BOJ_3077 임진왜란

- 난이도
  - 실버 3
- 유형
  - 브루트포스
- 풀이

  ```
  for i in range(N):
  answerMap[answer[i]] = i

  for i in range(N):
      for j in range(i+1,N):
          if answerMap[test[i]] < answerMap[test[j]]:
              cnt += 1
  ```

  dic으로 각 단어 우선순위를 설정하고 두개씩 비교하면서 점수를 체크한다.

---

## BOJ_1138 한 줄로 서기

- 난이도
  - 실버 2
- 유형
  - 구현
- 풀이
  ```
  for j in range(N):
      if cnt == more and wait[j] == 0:
          wait[j] = k
          break
      elif wait[j] == 0:
          cnt += 1
  ```
  cnt만큼 왼쪽에 사람이 있으면 넣어 주는데, 자리가 0이어야 한다

---

## BOJ_16922 로마 숫자 만들기

- 난이도
  - 실버 3
- 유형
  - 백트래킹
- 새로 배운 내용
  - 순서가 없기에 해당 index 다음부터 검사가능.
- 풀이
  ```
  def find(sum,i, k):
      if i==0:
          numSet.add(sum)
          return
      for j in range(k,len(arr)):
          find(sum+arr[j], i-1,j)
  ```
  k를 통해 검색 가지수를 줄여줌.

---

## BOJ_16974 레벨 햄버거

- 난이도
  - 실버 2
- 유형
  - 재귀
- 풀이
  ```
  def eat(n, x):
  if n == 0:
      return x
  if x == 1:
      return 0
  elif x <= 1 + burger[n-1]:
      return eat(n-1, x-1)
  elif x == 1 + burger[n-1] + 1:
      return patty[n-1] + 1
  elif x <= burger[n-1] + burger[n-1] + 1 + 1:
      return patty[n-1] + 1 + eat(n-1, (x-(burger[n-1]+2)))
  else:
      return patty[n]
  })
  ```
