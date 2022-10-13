class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

def insert(node, val):
    #만약 root가 비어있을 때
    #node를 root로 만듦
    if node is None:
        return node

    #만약 root의 값이 들어온 val보다 큰 경우
    if val <node.val:
        #작은값은 왼쪽 node로 이동
        node.left = insert(node.left, val)

    else:
        #root보다 크면 root의 오른쪽 node로 이동
        node.right = insert(node.right, val)

    #root값 리턴
    return node

def remove(root, val):
   #삭제를 위해 삭제할 위치를 찾기
   #삭제할 값이 root의 값보다 작을 경우
    if val < root.val:
        #왼쪽으로 이동
        root.left = remove(root.left.val)

    elif val > root.val :
        root.right = remove(root.right, val)
    
    #삭제할 노드를 찾아서 작업을 시작
    else:
        #케이스 여러가지로 나누기
        #1,2자식이 하나이거나 둘일경우 처리
        if root.left is None:
            temp_node = root.right
            return temp_node
        elif root.right is None:
            temp_node = root.left
            return temp_node

        #자식 노드가 2개인 경우
        #노드의 오른쪽에서 가장 작은 값을 찾기
        temp_node = minimum(root.right)

        #node의 값을 오른쪽에서 가장 작을 노드를 넣어줌
        root.val = temp_node.val

        '''temp_node.val 의 값을 삭제함
            root의 오른쪽에서 가장 왼쪽에 있는 값을 삭제 해주면 root에 temp_node.val의 값이 들어가고 temp_node를 삭제하면
            BST형태를 갖추게 됨'''
        root.right = remove(root.right,temp_node.val)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def minimum(node):
    #노드가 가장 왼쪽으로 가면 됨.
    while (node.left is not None):
        node = node.left

    return node.val


root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,40)
root = insert(root,20)
root = insert(root,80)
root = insert(root,70)
root = insert(root,90)

root = remove(root,50)
inorder(root)
