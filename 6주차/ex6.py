## 클래스의 함수 선언 부분 ##

class Node() :              #노드생성
    def __init__(self) :
        self.data = None
        self.link = None

def printNodes(start) :     #현재 노드 데이터 출력
    current = start         #(head 부터 노드의 끝까지)
    if current == None :
        return
    print(current.data, end=' ')
    while current.link != None :
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current, pre

    if head.data == findData :
        node = Node()
        node.data = insertData
        node.link = head
        return
    
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
        node = Node()
        node.data = insertData
        current.link = node

        insertNode("다연", "화사")
        printNodes(head)

        insertNode("사나", "솔라")
        printNodes(head)

        insertNode("재남", "문별")
        printNodes(head)