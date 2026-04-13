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