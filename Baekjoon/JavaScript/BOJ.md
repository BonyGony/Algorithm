# JavaScript Algorithm

## [2022.08.06]

- BOJ_1309 동물원

  - 난이도
    - 실버 1
  - 유형
    - dp
  - ## 풀이

    ```
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901;
    ```

    2개 -> 3
    4개 -> 322
    6개 -> 322 322 3
    8개 -> 322 32 32 322 32 32 322

- BOJ_11052 카드 구매하기

  - 난이도
    - 실버 1
  - 유형
    - dp
  - ## 풀이

    ```
    dp[i] = Math.max(dp[i], dp[i - j] + arr[j - 1]);
    ```

    i=1

    - 1번째 카드 + 카드 0개 선택

    i=2

    - 1번째 카드 + 카드 1개 선택
    - 2번째 카드 + 카드 0개 선택

    i=3

    - 1번째 카드 + 카드 2개 선택
    - 2번째 카드 + 카드 1개 선택
    - 3번째 카드 + 카드 0개 선택

## [2022.08.05]

- BOJ_14916 거스름돈

  - 난이도
    - 실버 5
  - 유형
    - dp
  - ## 풀이

    ```
    dp[1] = 999;
    dp[3] = 999;
    dp[i] = Math.min(dp[i - 2] + 1, dp[i - 5] + 1);
    ```

    1, 3은 거스름돈이 없다는 것을 999라는 큰 수를 이용해 없는 것으로 처리함.

- BOJ_9655 돌 게임

  - 난이도
    - 실버 5
  - 유형
    - dp
  - ## 풀이

    ```
    n % 2 === 0 ? "CY" : "SK"
    ```

    상근이가 무조건 먼저(1 아니면 3만 가능).

    1 -> 상근 : 1 => 상근 승

    2 -> 상근 : 1, 창영: 1 => 창영 승

    3 -> 상근 : 1 or 상근 : 3 => 상근 승

    4 -> 상근 : 1 or 상근 : 3, 창영 : 1 => 창영 승

    홀수일 때에는 상근, 짝수일 때에는 창영 승.

## [2022.08.04]

- BOJ_2002 추월

  - 난이도
    - 실버 1
  - 유형
    - Map
  - ## 풀이

    ```
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (carsMap.get(endCars[i]) > carsMap.get(endCars[j])) {
                count++;
                break;
            }
        }
    }
    ```

    carsMap에 순서를 기록하고 endCars 배열을 각각 비교해서 추월차량을 파악함.

## [2022.08.03]

- BOJ_20291 파일정리

  - 난이도
    - 실버 3
  - 유형
    - Map
  - 새로 배운 내용
    - Object.keys(obj), Object.values(obj), Object.entries(obj)는 배열을 리턴.
    - Map vs Obj
      1. Map
         - key로 여러 타입 가능.
         - map.size로 크기 빠르게 구함 : O(1).
         - 자체가 iterable함.
         - key에 순서가 있음.
      2. Obj
         - key로 문자열 가능.
         - size를 직접 구해야 함 : O(n).
         - 배열을 얻어 iterable하게 만들어야함.
         - key에 순서가 없고 충돌이 일어날 수 있음.
  - ## 풀이

    ```
    files.forEach((file) => {

    let [first, second] = file.split(".");

    if (filesObj[second]) {
      filesObj[second] += 1;
    } else {
      filesObj[second] = 1;
    }

    });

    const filesArr = Object.entries(filesObj).sort();
    ```

    해당 확장자가 있으면 +1, 없으면 1로 초기화.
    Object.entries(obj)로 배열로 만들고 sort() 해줌.

## [2022.08.02]

- BOJ_13414 수강신청
  - 난이도
    - 실버 3
  - 유형
    - Set
  - 새로 배운 내용
    - JS에서 Set은 순서 유지해 줌.
    - for문 중복 조건 가능.
  - ## 풀이
    ```
    studentIds.forEach(( studentId ) => {
        idSet.delete(studentId);
        idSet.add(studentId);
    })
    ```
    해당 Id를 삭제하고 추가하면 중복 없이 뒤에 추가됨.
