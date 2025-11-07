from src.Trees.Implementation.Binary_Search_Tree import BinaryNode, bst

def count_leaves(current: BinaryNode, cont: int = 0) -> int:

    if current is None:
        return cont

    if current.left is None and current.right is None:
        return cont + 1

    cont = count_leaves(current.left, cont)
    cont = count_leaves(current.right,cont)
    return cont

bst.print()

print(count_leaves(bst.root))


