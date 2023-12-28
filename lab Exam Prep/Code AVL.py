class treeNode(object):
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.h = 1

class AVLTree(object):
    def insert(self, root, key):
        if not root: # base case 
            return treeNode(key)
        elif key < root.value:
            root.l = self.insert(root.l, key)
        else:
            root.r = self.insert(root.r, key)

        root.h = 1 + max(self.getH(root.l),self.getH(root.r))

        balancefactor = self.getBF(root)

        if balancefactor > 1 and key < root.l.value:
            return self.RR(root)

        if balancefactor < -1 and key > root.r.value:
            return self.LR(root)

        if balancefactor > 1 and key > root.l.value:
            root.l = self.LR(root.l)
            return self.RR(root)

        if balancefactor < -1 and key < root.r.value:
            root.r = self.RR(root.r)
            return self.LR(root)

        return root

    def LR(self, z):
        y = z.r
        T2 = y.l

        y.l = z
        z.r = T2

        z.h = 1 + max(self.getH(z.l),self.getH(z.r))
        y.h = 1 + max(self.getH(y.l),self.getH(y.r))

        return y

    def RR(self, z):
        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getH(z.l),self.getHeight(z.r))
        y.h = 1 + max(self.getH(y.l),self.getH(y.r))

        return y

    def getH(self, root):
        if not root:
            return 0

        return root.h

    def getBF(self, root):
        if not root:
            return 0
        # bf formula
        return self.getH(root.l) - self.getH(root.r)

    def preOrder(self, root):
        if not root:
            return

        print("{0} ".format(root.value), end="")
        self.preOrder(root.l)
        self.preOrder(root.r)

# Usage Example
Tree = AVLTree()
root = None

root = Tree.insert(root, 1)
root = Tree.insert(root, 2)
root = Tree.insert(root, 3)
root = Tree.insert(root, 4)
root = Tree.insert(root, 5)
root = Tree.insert(root, 6)

# Preorder Traversal
print("Preorder traversal of the",
    "constructed AVL tree is")
Tree.preOrder(root)
print()
