from typing import Optional
from src.Trees.Implementation.Binary_Tree import BinaryTree, BinaryNode

def sum_sub_ranch(bt: BinaryTree, value: int, current: Optional[BinaryNode] = None, flag: bool = True, flag2: bool = True, lista1: Optional[list[int]] = None,  lista2: Optional[list[list[int]]] = None) -> list[int]:
    bt_aux = bt
    if flag:
        current = bt_aux.root
        lista1 = []
        lista2 = []
        flag = False

    if current is None:
        for i in range(1,len(lista1)+1):
            if sum(lista1[::-i]) == value:
                lista2.append(lista1[::-i])
        return []
    print(lista1)
    lista1.append(current.value)
    print(lista1)
    if current.left is None and current.right is None:
        lista1.pop(-1)



    print(lista1)

    sum_sub_ranch(bt, value, current.left, flag, flag2, lista1, lista2)
    sum_sub_ranch(bt, value, current.right, flag, flag2, lista1, lista2)

    return lista2

tree = BinaryTree()
tree.insert_by_level([1, 2, 3, None, 2, 6, None, 5,1,2,3,4,5,6,7,8,9])
tree.insert_parent_child(5,10)
tree.print()
print(sum_sub_ranch(tree, 20))


