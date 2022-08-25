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
