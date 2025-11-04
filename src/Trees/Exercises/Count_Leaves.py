from src.Trees.Implementation.Binary_Search_Tree import BinaryNode, bst

def count_leaves(current: BinaryNode) -> int:

    if current is None:
        return 0

    if current.left is None and current.right is None:
        return 1

    return count_leaves(current.left) + count_leaves(current.right)

bst.print()
print(count_leaves(bst.root))


