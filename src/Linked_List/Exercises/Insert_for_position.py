from src.Linked_List.Implementation.DoublyLinkedList import DoublyLinkedList, NodeDoubly

dll = DoublyLinkedList()

def insert(value: int, pos: int):
    current = dll.head
    new_node = NodeDoubly(value)
    if pos >= dll.size:
        dll.tail.next = new_node
        new_node.prev = dll.tail
        dll.tail = new_node
    elif pos == 0:
        new_node.next = dll.head
        dll.head = new_node
    else:
        for _ in range(pos):
            current = current.next
        current.prev.next = new_node
        new_node.next = current
        new_node.prev = current.prev
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
insert(200, 4)
print(dll)
