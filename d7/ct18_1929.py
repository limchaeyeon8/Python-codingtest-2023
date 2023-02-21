# 백준 1929 - 소수 구하기

import math
M, N = map(int, input().split())
A = [0] * (N+1)         # 초기화

for i in range(2, N+1):
    A[i] = i                # 인덱스를 채워넣기

for i in range(2, int(math.sqrt(N)) + 1):   # N의 제곱근까지만 수행
    if A[i] == 0:
        continue
    # i == 2 /// 4 + 2 + 2 + 2 
    # i == 3 /// 6 + 3 + 3 + 3
    for j in range(i+i, N+1, i):            # 배수로 지우기
        A[j] = 0                # 더 이상 소수가 아님 -> 지워버림

for i in range(M, N+1):
    if A[i] != 0:
        print(A[i])