class MinStack:

    def __init__(self):
        self.stack = []
        self.p = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        item = min(val, self.p[-1] if self.p else val)
        self.p.append(item)
        

    def pop(self) -> None:
        self.stack.pop()
        self.p.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.p[-1]
        
