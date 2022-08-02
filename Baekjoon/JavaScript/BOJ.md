# JavaScript Algorithm

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
