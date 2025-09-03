class Stack:
    def __init__(self):
        self.stack: list = []

    def push(self,objeto):
        self.stack.append(objeto)

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError ("Empty Stack")
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            raise IndexError("Empty Stack")
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        return f"{self.stack}"
