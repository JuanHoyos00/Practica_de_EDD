from src.Trees.Implementation.Binary_Tree import BinaryNode, BinaryTree


def search_string(current: BinaryNode, string: str, position: int = 0) -> bool:
    if position == len(string):
        return True

    if current is None:
        return False


    if current.value == string[position]:
        if search_string(current.left, string,position+1) or search_string(current.right, string,position+1):
            return True

    if search_string(current.left,string,0):
        return True

    elif search_string(current.right, string, 0):
        return True

    return False

bt = BinaryTree()
bt.insert_by_level(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',])
bt.insert_parent_child('k','l')
bt.insert_parent_child('k','z')


bt.print()
print(search_string(bt.root,'bek'))