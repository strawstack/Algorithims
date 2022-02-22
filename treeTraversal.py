class TreeTraversal:

    def __init__(self):
        self.lst = []

    def preOrder(self, node):
        if node == None:
            return        
        self.lst.append(node)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if node == None:
            return
        self.inOrder(node.left)
        self.lst.append(node)
        self.inOrder(node.right)

    def postOrder(self, node):
        if node == None:
            return        
        self.postOrder(node.left)
        self.postOrder(node.right)
        self.lst.append(node)