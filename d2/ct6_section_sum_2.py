# 2차원 구간합
# 백준 11660번

import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))         # 2차원 행렬크기, 절의 갯수
#print(n)
#print(m)

A = [ [0] * ( n + 1 ) ]
#print(A)
D = [ [0] * ( n + 1 ) for _ in range( n + 1 )]  # for문에 들어가는 언더바는 아무 작업도 수행하지 않음
#print(D)

# 2차원 합배열 D 만듦
for i in range(n):
    rows = list(map(int, input().split()))
    A_row = [0] + rows
    A.append(A_row)

#print(A)

# 2차원 합배열 D 만듦       0(1024x1024) 백만
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] +  D[i-1][j] - D[i-1][j-1] + A[i][j]

# 구간합
for _ in range(m):      # _ 는 반복문에 들어오는 (m에 들어가는) 변수값(0, 1, 2)들은 안 사용하겠다
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)