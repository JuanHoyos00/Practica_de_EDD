class Queue:
    def __init__(self):
        self.queue: list = []

    def enqueue(self,objeto):
        self.queue.append(objeto)

    def dequeue(self):
        if len(self.queue) == 0:
            raise IndexError ("Empty Queue")
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            raise IndexError("Empty Queue")
        return self.queue[0]

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        return f"{self.queue}"
