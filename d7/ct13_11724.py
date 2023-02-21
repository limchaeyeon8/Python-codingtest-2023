# 백준 11724 - 연결요소 개수 구하기

import sys
# 재귀호출할 때 파이썬에는 1000번까지 제한이 있음,,
# 그 제한을 
sys.setrecursionlimit(10**6)    # 100만번
# 입력받는 속도가 느리기 때문에 백준에서 그냥 돌리면 입력오류 발생가능(대부분)
input = sys.stdin.readline

n, m = map(int, input().split())    # 6, 5
A = [[] for _ in range(n+1)]        # 행 x, 열 7개 2차원 리스트
visited = [False] * (n+1)           # [0,1,2,3,4,5,6]

# DFS 함수 만들기 (재귀함수)
def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:          # 방문을 안 했다면
            DFS(i)

for _ in range(m):                  # 에지 개수만큼
    s, e = map(int, input().split())

    A[s].append(e)              # 무방향이기 때문에 양쪽 에지 추가
    A[e].append(s)

count = 0

for i in range(1, n+1):          # 노드 1부터 n번까지(0 안 씀)
    if not visited[i]:
        count += 1
        DFS(i)


print(count)