# 백준 11725 - 트리 부모 찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())                    # 7
visited = [False] * (N + 1)
tree = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)

for _ in range(1, N):
    n1, n2 = map(int, input().split())      # 부모 자식 순서 X
    tree[n1].append(n2)
    tree[n2].append(n1)

#   DFS 탐색 함수
def DFS(number):
    visited[number] = True          # 방문
    for i in tree[number]:
        if not visited[i]:          # 방문 안 했으면
            answer[i] = number      # DFS를 수행하면서 부모 노드를 정답 리스트에 저장
            DFS(i)

DFS(1)          # 부모 노드부터 DFS 시작

for i in range(2, N+1):             # 1번은 루트노드이기 때문에 부모 없음
    print(answer[i])                # 2번 노드부터의 부모들 나열