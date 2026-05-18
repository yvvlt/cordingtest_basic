class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.name, end='->')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.name, end='->')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.name, end='->')

# 트리 구성
화사 = Node('화사')
솔라 = Node('솔라')
문별 = Node('문별')
휘인 = Node('휘인')
쯔위 = Node('쯔위')
선미 = Node('선미')
다현 = Node('다현')
사나 = Node('사나')

# 트리 연결
화사.left = 솔라
화사.right = 문별

솔라.left = 휘인
솔라.right = 쯔위

문별.left = 선미

휘인.right = 다현

선미.right = 사나

# 순회 출력
print("전위 순회 : ", end='')
preorder(화사)
print("끝")

print("중위 순회 : ", end='')
inorder(화사)
print("끝")

print("후위 순회 : ", end='')
postorder(화사)
print("끝")