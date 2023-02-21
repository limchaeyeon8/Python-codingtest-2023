# 백준 1920 - 원하는 정수찾기

N = int(input())        # 5
A = list(map(int, input().split()))     # 4 1 5 2 3
A.sort()                                # 파이썬 리스트에서 제공하는 기본 정렬

M = int(input())
targetList = list(map(int, input().split()))    # 1 3 7 9

for i in range(M):
    find = False    ####
    target = targetList[i]              # 처음 값 1
    # 이진 탐색
    start = 0 
    end = N - 1 
    while start <= end:
        midle = (start + end) // 2      # 중앙을 가리키는 인덱스
        midVal = A[midle]               # 중앙에 있는 값
        if midVal > target:             # 오른쪽 날림
            end = midle - 1
        elif midVal < target:           # 왼쪽 날림
            start = midle + 1
        else:                           # 값을 찾음
            find = True
            break

    if find:
        print(1)
    else:
        print(0)