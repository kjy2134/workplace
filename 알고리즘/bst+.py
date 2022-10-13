class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

def insert(node, val):
    #만약 root가 비어있을 때
    #node를 root로 만듦
    if node is None:
        return node(val)

root = None
root  = insert(root, 50)
print(root)