class DepthFirstSearch:

    def __init__(self):
        self.lst = []
    
    def search(self, node, target):
        if node.value == target:
            self.lst.append(target)
        else:
            self.lst.append(node.value)

        if node.left != None:
            self.search(node.left, target)
        
        if node.right != None:
            self.search(node.right, target)