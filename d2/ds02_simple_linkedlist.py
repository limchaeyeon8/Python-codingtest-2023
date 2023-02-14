# 단순 연결리스트 구현

class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None

# 전역 변수
memory = []                 # lists()
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

def printNodes(start):
    current = start
    if current == None:
        return
    
    print(current.data, end=' -> ')
    while current.link != None:
        current = current.link

        if current.link == None:
            print(current.data)
        else:
            print(current.data, end=' -> ')

def insertNode(findData, insertData):
    global memory, head, current, pre

    # 맨 앞 노드 삽입
    if head.data == findData:       # 첫노드 앞
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head      # 커런트를 제일 앞으로 땡겨줌
    while current.link != None:     # 중간 노드 삽입
        pre = current
        current = current.link

        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    # current.link == None 까지 온 것
    node = Node()
    node.data = insertData
    current.link = node
    return

# 노드삭제
def deleteNode(deleteData):
    global memory, pre, current, head
    if head.data == deleteData:     # 첫번째 노드 삭제
        current = head
        head = head.link            # 두번째 노드로 변경
        del(current)
        return
    
    current = head
    while current.link != None:     # 첫번째 이외 노드 삭제
        pre = current               # 모두 첫번째 노드 가리킴
        current = current.link      # 두번째 노드를 가리킴
        if current.data == deleteData:
            pre.link = current.link # current가 가리키는 노드를 pre가 가리키도록(삭제)
            del(current)            # 메모리에서 삭제
            return

# 노드검색
def findNode(findData):
    global memory, pre, current, head

    current = head                  # 첫번째 노드부터
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link      # 다음 노드
        if current.data == findData:
            return current
        
    return Node()                   # 빈노드 반환

if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0]        # 인덱스 0 == 다현
    head = node
    memory.append(node)

    for data in dataArray[1:]:      # 두번째 노드 이후 4번 반복
        pre = node
        node = Node()
        node.data = data            # 정연, 쯔위, 사나, 지효 순
        pre.link = node
        memory.append(node)

    printNodes(head)                # 전체 출력


    print('노드 추가 ----')

# 순서 바뀌어도 문제 없음

    insertNode('다현', '화사')      # 다현 앞 화사 추가
    printNodes(head)

    insertNode('사나', '솔라')      # 중간 노드 추가
    printNodes(head)

    insertNode('채연', '문별')      # 맨 마지막 노드 추가
    printNodes(head)

    print('노드 삭제 ----')

    deleteNode('화사')
    printNodes(head)

    deleteNode('지효')
    printNodes(head)

    deleteNode('채연')      # 데이터 삭제X
    printNodes(head)

print('노드 검색 ----')

result = findNode('정연')
if result.data != None:
    print('데이터 찾았습니다')
else:
    print('검색된 데이터가 없습니다')

result = findNode('채연')
if result.data != None:
    print('데이터 찾았습니다')
else:
    print('검색된 데이터가 없습니다')