class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

        
# Root left right
def preorder_traversal(root):
    if root:     
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Left Root Right
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)
                
# Left Right Root
def postorder_traversal(root):
    if root:      
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")
        
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right.left = Node(13)
print("Preorder Traversal:")
preorder_traversal(root)
print("\n")
print("Inorder Traversal:")
inorder_traversal(root)
print("\n")
print("Postorder Traversal:")
postorder_traversal(root)
