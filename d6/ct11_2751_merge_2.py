# 백준 2751 - 수정렬하기 2

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
A = [0] * int(N + 1)

for i in range(1, N+1):
    A[i] = int(input())

A.sort()

for i in range(1,  N+1):
    print(A[i])