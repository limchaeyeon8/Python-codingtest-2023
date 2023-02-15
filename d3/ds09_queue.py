# 큐 구현
# 큐가 꽉차면 하나씩 빼는 형태

# 글로벌(전역변수)
SIZE = 0
queue = []
front = rear = -1

# Queue Full 체크
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE -1):
        return False
    elif (rear == SIZE -1) and (front == -1):
        return True
    else:
        # deQueue를 한 뒤 빈자리를 채우는
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1           # 1씩 감소
        return False
    
# Queue Empty 체크
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False
    
def enQueue(data):          # Queue에 데이터 추가
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is Full')
    else:
        rear += 1
        queue[rear] = data

def deQueue():              # Queue 데이터 추출(*꺼내버림)
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    else:
        front += 1
        data = queue[front]
        queue[front] = None
    
        # deQueue를 한 뒤 빈자리를 채우는
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1           # 1씩 감소
 
        return data
    
def peek():                  # Queue front+1 위치값 확인
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    else:
        return queue[front+1]
    

# 메인 엔트리
if __name__ == '__main__':
    SIZE = int(input('큐 사이즈 입력 > '))
    queue = [None for _ in range(SIZE)]

    while True:
        select = input('삽입(I)/ 추출(E)/ 확인(V)/ 종료(X) >> ')
        if select.lower() == 'x':
            break
        elif select.lower() == 'i':
            data = input('입력 데이터 >> ')
            enQueue(data)
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'e':
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'v':
            data == peek()
            print(f'확인 상태 : {data}')
            print(f'큐 상태 : {queue}')

        else:
            continue

    print('===큐 프로그램 종료===')
