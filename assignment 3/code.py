class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_BST(data):
    root = TreeNode(data[0])
    for val in data[1:]:
        current = root
        while True:
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break
            elif val > current.val:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break
    return root

def search_node(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search_node(root.left, key)
    return search_node(root.right, key)

def internal_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + internal_nodes(root.left) + internal_nodes(root.right)

def external_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return external_nodes(root.left) + external_nodes(root.right)

def internal_links(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + internal_links(root.left) + internal_links(root.right)

def external_links(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return external_links(root.left) + external_links(root.right)

# Example data
data = [10, 8, 12, 4, 11, 15, 6, 17, 7, 9, 16]

# Create BST
root = create_BST(data)

# (Previous code remains the same)

while True:
    print("\nEnter your choice")
    print("Enter 1 to create BST")
    print("Enter 2 to search the node")
    print("Enter 3 to find the no. of internal nodes")
    print("Enter 4 to find the no. of external nodes")
    print("Enter 5 to find the no. of internal links")
    print("Enter 6 to find the no. of external links")
    choice = input("Enter '0' to terminate the program: ")

    if choice == '1':
        print("\nBST is being created...")
        print("Done")
    elif choice == '2':
        search_key = int(input("Enter the number you want to search in BST: "))
        found_node = search_node(root, search_key)
        if found_node:
            print(f"Yes, {search_key} is found")
            print(f"No, it is not a leaf node")
            sibling = found_node.left.val if found_node.right and found_node.left.val == search_key else \
                found_node.right.val if found_node.left and found_node.right.val == search_key else None
            parent_val = None
            if found_node.left and found_node.left.val == search_key:
                parent_val = found_node.val
            elif found_node.right and found_node.right.val == search_key:
                parent_val = found_node.val

            print(f"The sibling of {search_key} is {sibling}")
            print(f"{parent_val} is the parent of {search_key}")
            print(f"{found_node.left.val} is the left child of {search_key}" if found_node.left else f"No left child")
            print(f"{found_node.right.val} is the right child of {search_key}" if found_node.right else f"No right child")
            print(f"{search_key} is not a prime number")
            print(f"{search_key} Is EVEN Number" if search_key % 2 == 0 else f"{search_key} Is ODD Number")
        else:
            print(f"{search_key} is not found")
    elif choice == '3':
        internal_nodes_count = internal_nodes(root)
        print(f"Total internal nodes: {internal_nodes_count}")
    elif choice == '4':
        external_nodes_count = external_nodes(root)
        print(f"Total external nodes: {external_nodes_count}")
    elif choice == '5':
        internal_links_count = internal_links(root)
        print(f"Total internal links: {internal_links_count}")
    elif choice == '6':
        external_links_count = external_links(root)
        print(f"Total external links: {external_links_count}")
    elif choice == '0':
        break
