# 백준 1541 - 최솟값을 만드는 괄호 배치 찾기
# 그리디

answer = 0
A = list(map(str, input().split('-')))      # - 기준으로 잘라서 문자열로 리스트

def mySum(i):                   # - 로 나눈 각 수직 문자열 합 구하기 함수
    result = 0
    temp = str(i).split('+')    # + 기준으로 수식 자름  # 78+45

    for k in temp:
        result += int(k)        # '78' 같은 문자열이므로 int()
    
    return result

for s in range(len(A)):
    temp = mySum(A[s])

    if s == 0:
        answer += temp          # 맨처음
    else:
        answer -= temp          

print(answer)
