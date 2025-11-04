from src.Trees.Implementation.Binary_Tree import BinaryNode, BinaryTree


def search_string(current: BinaryNode, string: str, position: int = 0) -> bool:
    if current is None:
        return False

    if position == len(string):
        return True

    if current.value == string[position]:
        if position == len(string)-1:
            return True
        flag = search_string(current.left, string, position + 1)
        if not flag:
            flag = search_string(current.right, string, position + 1)
        return flag

    if search_string(current.left, string, 0):
        return True

    if search_string(current.right, string, 0):
        return True

    return False

bt = BinaryTree()
bt.insert_by_level(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
bt.print()
print(search_string(bt.root,'abh'))