class NodeSingly:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value) -> None:
        node = NodeSingly(value)
        if self.size == 0:
            self.head = self.tail = node
            node.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            node.next = self.head
        self.size += 1

    def __repr__(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return "-".join(values)