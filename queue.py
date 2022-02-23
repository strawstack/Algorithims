class Queue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def pop(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                self.out_stack.append(self.in_stack.pop())
        
        if len(self.out_stack) != 0:
            return self.out_stack.pop()
        else:
            return None

    def push(self, item):
        self.in_stack.append(item)
    
    def size(self):
        return len(self.in_stack) + len(self.out_stack)