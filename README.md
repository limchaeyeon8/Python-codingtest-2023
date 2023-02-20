# Python-codingtest-2023
파이썬 코딩테스트 리포지토리

# 1일차
1. 코딩테스트 소개
2. 코딩테스트 학습
  - [x] 자료구조 - 배열 / 리스트
  - [x] 구간합
  
# 2일차
! 파이썬 파일명에는 '_' 사용 권장

1. 코딩테스트 학습
  - 구간합 2
  - [x] 자료구조 다시
    - [x] 연결리스트
    - [x] 스택
  - [x] pythonds 스택 확인

# 3일차
 1. 코딩테스트 학습
  - 자료구조
    - [x] 큐
    - pythonds 스택 확인
    - [x] 이진트리
      - 삭제는 연결리스트 삭제와 유사
    - 그래프

  # 4일차
1. 코딩테스트 학습
  -자료구조
    - [x] 그래프 계속
    - [x] 재귀호출
    - 정렬 소개

# 5일차
1. 코딩테스트 학습
  - 자료구조
    - [x] 정렬
    - [x] 검색
    - [x] 다이나믹 프로그래밍 / 피보나치 실행시간 비교

# 6일차
1. 코딩테스트 학습
  - 자료구조 학습
    - [x] 덱(Deque)
  - 코딩테스트 알고리즘
    - 백준
    - 프로그래머스

```python
# 백준 11003 - 최솟값 찾기 1

from collections import deque
# from pythonds.basic.deque import Deque        # <--대체가능

myDeque = deque()
N, L = map(int, input().split())        # 12 3
now = list(map(int, input().split()))   # 1 5 2 3 6 2 3 7 3 5 2 6


# 새값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거
# 시간복잡도를 줄임
# (정렬 갯수는 최대 5백만개이기 때문에 ㄴㄴ)

for i in range(N):
    while myDeque and myDeque[-1][0] > now[i]:      # 인덱스가 현재 들어있는 값보다 크면 
        myDeque.pop()                               # 빼버린다
    myDeque.append((now[i], i))
    if myDeque[0][1] <= i - L:                  # 범위를 벗어난 값도 덱에서 제거
        myDeque.popleft()
    print(myDeque[0][0], end=' ')           # 무조건 최소값((( 'min()' 과 동일)))
```

# 7일차
1. 코딩테스트 학습

# 8일차
1. 코딩테스트 학습