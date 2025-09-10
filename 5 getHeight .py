class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
def getHeight(root):
    if root is None:
        return 0
    return 1 + getHeight(root.left) + getHeight(root.right)
root = None

list1=[10,5,15,3,7]
for key in list1:
    root = insert(root, key)

print("Height of BST:", getHeight(root))