from src.Trees.Implementation.Binary_Search_Tree import BinaryNode, bst

def count_nodes_at_level(current: BinaryNode, k:int, i: int = 0, counter: int = 0) -> int:

    if i == k:
        if current is not None:
            counter += 1
            return counter
        else:
            return counter

    if current is None:
        return counter

    counter = count_nodes_at_level(current.left, k, i+1, counter)
    counter = count_nodes_at_level(current.right, k, i + 1, counter)
    return counter

print(count_nodes_at_level(bst.root, 0))
bst.print()