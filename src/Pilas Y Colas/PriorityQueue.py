class PriorityQueue:
    def __init__(self,priority: str):
      self.queue: list[int] = []
      self.priority: str = priority

    def enqueue(self, objeto):
      if self.priority == "MAX":
        self.queue.append(objeto)
        self.queue.sort(reverse = True)
      elif self.priority == "MIN":
        self.queue.append(objeto)
        self.queue.sort()
      else:
        print("Ingresa una prioridad válida")

    def dequeue(self):
      if len(self.queue) == 0:
        raise IndexError("Empty Queue")
      return self.queue.pop(0)

    def peek(self):
      if len(self.queue) == 0:
        raise IndexError("Empty Queue")
      return self.queue[0]

    def __len__(self):
      return len(self.queue)

    def __repr__(self):
      return f"{self.queue}"