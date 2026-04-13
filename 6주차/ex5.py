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