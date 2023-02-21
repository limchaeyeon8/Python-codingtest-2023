# 백준 1260 - DFS와 BFS

from queue import Queue     # Deque 안 써도 가능
N, M, Start = map(int, input().split())
A = [[] for _ in range(N + 1)]          # 인접 리스트

for _ in range(M):          # 에지수만큼
    s, e = map(int, input().split())
    A[s].append(e)          # 무방향 에지
    A[e].append(s)

for i in range(N + 1):
    A[i].sort()             # 번호 작은 노드부터 방문

visited = [False] * (N + 1)

def DFS(v):
    print(v, end=' ')
    visited[v] = True       # 방문
    for i in A[v]:
        if not visited[i]:  # True가 아니라면
            DFS(i)

# BFS 함수 정의
def BFS(v):
    q = Queue()
    q.put(v)
    visited[v] = True
    while q.empty() != True:            ## 주의        # q가 빌 때까지
        now = q.get()
        print(now, end=' ')
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                q.put(i)

# DFS 실행
visited = [False] * (N + 1)
DFS(Start)
print()
# BFS 실행
visited = [False] * (N + 1)
BFS(Start)
print()