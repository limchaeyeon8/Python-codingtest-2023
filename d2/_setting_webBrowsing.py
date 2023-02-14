# 스택 활용

import ds04_stack as st

import webbrowser       # 웹사이트 띄우기 위해 사용하는 모듈
import time

# 함수선언

st.SIZE = 100
st.stack = [None for _ in range(st.SIZE)]
st.top = -1

if __name__ == '__main__':
    urls = ['github.com', 'drive.google.com/drive/folders/1lks7MB87mcNVvs_oVxpNZRRqwdY2I9_M', 'www.acmicpc.net', 'programmers.co.kr']

    for url in urls:
        st.push(url)
        webbrowser.open(f'https://{url}')
        print(url, end=' --> ')
        time.sleep(0.1)       # 0.1초 대기

    input('꺼지지 말고 기다려!')