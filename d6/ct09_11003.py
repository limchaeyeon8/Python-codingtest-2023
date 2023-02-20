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

        