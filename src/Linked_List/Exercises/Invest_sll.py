from src.Linked_List.Implementation.SinglyLinkedList import SinglyLinkedList

sll = SinglyLinkedList()
def invest(sll: SinglyLinkedList, tail = None):

    if not tail:
        tail = sll.tail

    head = sll.tail
    cont = sll.size - 2
    for _ in range(sll.size-1):
        current = sll.head

        for _ in range(cont):
            current = current.next
        cont -= 1
        tail.next = current
        tail = current
    sll.head = head
    sll.tail = tail
    sll.tail.next = None

sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.append(7)
sll.append(8)
sll.append(9)
sll.append(10)
sll.append(11)
sll.append(12)
sll.append(13)
sll.append(14)
sll.append(15)
print(sll)
invest(sll)
print(sll)
print(sll.tail.value)