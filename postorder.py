class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
def postorder(root):
    if root:
        postorder(root.left)       
        postorder(root.right)      
        print(root.key, end=" ")   
 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
 
print("Postorder Traversal:")
postorder(root)