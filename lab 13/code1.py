class TreeNode:
    def __init__(self, item):
        self.info = item
        self.left = None
        self.right = None

def insert(root, item):
    if root is None:
        return TreeNode(item)
    if item < root.info:
        root.left = insert(root.left, item)
    elif item > root.info:
        root.right = insert(root.right, item)
    return root

def retrieve(root, item):
    if root is None:
        return False
    if item < root.info:
        return retrieve(root.left, item)
    
    
    elif item > root.info:
        return retrieve(root.right, item)
    else:
        return True

def inorder(root):
    if root:
        inorder(root.left)
        print(root.info, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.info, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        
        print(root.info, end=" ")

# Creating the tree and performing operations
tree = None
tree = insert(tree, 30)
tree = insert(tree, 20)
tree = insert(tree, 40)
tree = insert(tree, 25)
tree = insert(tree, 45)
tree = insert(tree, 35)
tree = insert(tree, 5)
tree = insert(tree, 50)
tree = insert(tree, 60)
tree = insert(tree, 18)
tree = insert(tree, 15)

found = retrieve(tree, 25)
if found:
    print("Number Found")
else:
    print("Not Found")

print("Inorder =", end=" ")
inorder(tree)
print("\nPreorder =", end=" ")
preorder(tree)
print("\nPostorder =", end=" ")
postorder(tree)
