class Node() :              #노드생성
    def __init__(self) :
        self.data = None
        self.link = None

def findNode(findData) :
    global memory, head, current, pre

    current = head
    if current.data == findData:
        return current
    while current.link != None :
        current = current.link
        if current.data == findData:
            return current
        return Node()
    
fNode = findNode("다현")
print(fNode.data)

fNode = findNode("쯔위")
print(fNode.data)

fNode = findNode("재남")
print(fNode.data)