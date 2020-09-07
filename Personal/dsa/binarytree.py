class node:
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None

class binarySearchTree:
    def __int__(self):
        self.root = None

    def insert(self, nodes, val):
        if self.root is None:
            newNode = node(val)
            self.root = newNode
        else:
            if(nodes is None):
                newNode = node(val)
                nodes = newNode
                return newNode
            if nodes.value > val:
                nodes.right = self.insert(nodes.right, val)
            else:
                nodes.left = self.insert(nodes.left, val)

    
bst = binarySearchTree()
bst.
bst.insert(bst.root, 5)
bst.insert(bst.root, 6)


