class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        
    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)

def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

root = TreeNode(4)
root.insert(5)
root.insert(8)
root.insert(18)
root.insert(17)
root.insert(13)
root.insert(48)

print("Inorder Traversal:")
inorder(root)
print("\n")

print("Preorder Traversal:")
preorder(root)
print("\n")

print("Postorder Traversal:")
postorder(root)
