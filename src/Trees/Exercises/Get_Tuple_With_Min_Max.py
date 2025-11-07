from src.Trees.Implementation.Binary_Search_Tree import BinarySearchTree, BinaryNode
import random as rd

def get_tuple_with_min_max(bst_: BinarySearchTree, k: int, a: int = -1, b: int = -1, current: BinaryNode|None = None, flag: bool = True):
    if flag:
     current = bst_.root
     flag = False

    if current is None:
     return a,b

    if current.value == k:
        if current.left:
            a_current = current.left
            while a_current.right is not None:
                a_current = a_current.right
            a = a_current.value

        if current.right:
            b_current = current.right
            while b_current.left is not None:
                b_current = b_current.left
            b = b_current.value
        return a,b
    a,b = get_tuple_with_min_max(bst_, k, a, b, current.left, flag)
    a,b = get_tuple_with_min_max(bst_, k, a, b, current.right, flag)

    return a,b

bst = BinarySearchTree()
rd.seed(1)
for _ in range(10):
    bst.insert(rd.randint(1,1000))

bst.print()
print(get_tuple_with_min_max(bst,13800))
