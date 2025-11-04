from typing import Any
from src.Trees.Implementation.Binary_Search_Tree import BinaryNode, bst


def delete_node(value: Any, current: BinaryNode) -> bool:

    if current is None:
        return False

    if current.left.value == value:
        current.left = current.left.left
        current.right = current.left.right
        return True

    if current.right.value == value:
        current.left = current.right.left
        current.right = current.right.right
        return True

    if delete_node(value, current.left):
        return True

    if delete_node(value, current.right):
        return True

    return False
bst.print()
print(delete_node(73, bst.root))
bst.print()