# 프로그래머스 템플릿 소스
# 코딩테스트 입문  -  배열의 평균값

def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    
    return answer / len(numbers)

#if __name__ == '__main__':
#    numbers = [1,2,3,4,5,6,7,8,9,10]
#    print(solution(numbers))

#    numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#    print(solution(numbers))
