class MinStack:

    def __init__(self):
        self.stack = []
        self.min_elems = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_elems.append(val)
        else:
            if val <= self.min_elems[-1]:
                self.min_elems.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack[-1] == self.min_elems[-1]:
            self.min_elems.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_elems[-1]
        
