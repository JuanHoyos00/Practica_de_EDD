class NodeSingly:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value) -> None:
        node = NodeSingly(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def __repr__(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return "-".join(values)

