# 최대 공약수 gcd()

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)   # 재귀함수 형태로 구현
        

a, b = map(int, input().split())
result = gcd(a, b)
print(result)

# while result > 0:
#     print(1, end='')
#     result -= 1