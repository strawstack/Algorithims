from queue import Queue

class BreadthFirstSearch:

    def __init__(self):
        pass
    
    # returns list of nodes in order of search
    def search(self, root):

        lst = []

        seen = {}
        q = Queue()
        q.push(root)

        while q.size() != 0:
            node = q.pop()

            if node.value in seen:
                continue

            seen[node.value] = True

            # Visit current node
            lst.append(node)

            # Add children to queue
            if node.left != None and node.left.value not in seen:
                q.push(node.left)
            
            if node.right != None and node.right.value not in seen:
                q.push(node.right)
        
        return lst