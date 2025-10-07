from src.Linked_List.Implementation.SinglyLinkedList import SinglyLinkedList

sll = SinglyLinkedList()

def delete_from_sll(sll: SinglyLinkedList, value: int) -> None:
    new = sll.head

    if new.value == value:
        if not new.next:
            sll.tail = sll.head = None

        else:
            sll.head = new.next

    else:
        while  new.next:

            if new.next.value == value:
                if new.next.next is None:
                    new.next = None
                    sll.tail = new
                    return

                else:
                    new.next = new.next.next
                    return
            else:
                new = new.next


sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.append(7)
sll.append(5)


delete_from_sll(sll,5)
print(sll)


