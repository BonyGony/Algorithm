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
