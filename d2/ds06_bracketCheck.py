# 수식 괄호 유효성 여부 확인

import ds04_stack as st

def chckBracket(expr):
    for ch in expr:
        if ch in '({[<':         # 여는 괄호 스택 추가
            st.push(ch)

        elif ch in ')}]>':
            out = st.pop()       # 여는 괄호 스택에서 추출
            if ch == ')' and out == '(':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
            
        else:
            pass

    if st.isStackEmpty():
        return True
    else:
        return False
    

st.SIZE = 10
st.stack = [None for _ in range(st.SIZE)]

if __name__ == '__main__':
    exprArry = ['(a+b)', ')a+b(', '(a*b)+(c/d)', '(a+b]', '(<a+{b-c}/[c**d]>)']

    for expr in exprArry:
        top = -1
        print(expr, '==>', chckBracket(expr))