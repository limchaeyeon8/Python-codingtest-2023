# 입력속도를 개선하기 위해 사용 // 단, 주피터노트북에서는 실행불가
import sys
InPut = sys.stdin.readline      # 이부분이 없으면 백준 시간 초과!!!


N, M = tuple(map(int, InPut().rstrip().split()))     # 두 값 한 번에 받을 때
numbers = list(map(int, InPut().rstrip().split()))

sums = [0]      ##### 핵심!!!
temp = 0

for i in numbers:
    temp = temp + i 
    sums.append(temp)

for i in range(M):
    x, y = tuple(map(int, InPut().split()))
    print(sums[y] - sums[x - 1])