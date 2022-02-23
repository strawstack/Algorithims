class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def getTree(height):
    root = Node()
    addChildNodes(root, height - 1)
    return root

def addChildNodes(node, height):
    if height <= 0: 
        return None

    node.left = Node()
    node.right = Node()

    addChildNodes(node.left, height - 1)
    addChildNodes(node.right, height - 1)

