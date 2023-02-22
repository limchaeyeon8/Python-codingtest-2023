# 백준 1717 - 집합 표현하기
# 유니온 파인드

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
parent = [0] * (N + 1)          # [0 for _ in range(N + 1)]

def find(a):                    # find 연산(제일중요)
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 재귀호출 => 경로압축 ===> 시간 복잡도 줄일 수 있음
        return parent[a]
    
def union(a, b):                # 대표 노드끼지 합치기
    a = find(a)
    b = find(b)
    if a != b:                  # 같으면 아무 것도 안 함
        # 0 7 6 입력시 생기는 문제?해결
        if a < b:
            parent[b] = a
        else:
            parent[a] = b    

def checkSame(a, b):            # 둘이 같은 집합인지
    a = find(a)
    b = find(b)
    if a == b: return True
    else: return False

for i in range(0, N + 1):
    parent[i] = i   # 1,1  2,2  3,3  4,4  5,5  6,6  7,7

for i in range(M):
    question, a, b = map(int, input().split())      # 0 1 3 or 1 1 7
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print('YES')
        else:
            print('NO')