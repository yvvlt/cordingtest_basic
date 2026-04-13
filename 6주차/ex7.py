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

def deleteNode(deleteData) :
    global memory, head, current, pre

    if head.data == deleteData :
        current = head
        head = head.link
        del(current)
        return
    
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            return
        
deleteNode("다현")
printNodes(head)

deleteNode("쯔위")
printNodes(head)

deleteNode("지효")
printNodes(head)

deleteNode("재남")
printNodes(head)

