# JavaScript Algorithm

## [2022.08.02]

- BOJ_13414 수강신청
  - 난이도
    - 실버 3
  - 유형
    - Set
  - 새로 배운 내용
    - JS에서 Set은 순서 유지해 줌.
    - for문 중복 조건 가능.
  - 풀이
    -
    ```
    studentIds.forEach(( studentId ) => {
        idSet.delete(studentId);
        idSet.add(studentId);
    })
    ```
    해당 Id를 삭제하고 추가하면 중복 없이 뒤에 추가됨.
