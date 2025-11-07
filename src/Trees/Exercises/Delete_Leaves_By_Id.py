from src.Trees.Implementation.Binary_Search_Tree import BinarySearchTree, BinaryNode
import random as rd
def delete_leaves_by_id(bst_: BinarySearchTree, identifiers: list[int], current: BinaryNode|None = None, num_leaf: int = 0, flag: bool = True):
    if flag:
        current = bst_.root
        flag = False

    if current is None:
        return num_leaf
    else:
        if current.left:
            if current.left.left is None and current.left.right is None:
                num_leaf += 1
                if num_leaf in identifiers:
                    current.left = None
            num_leaf = delete_leaves_by_id(bst_, identifiers, current.left, num_leaf, flag)
        if current.right:
            if current.right.left is None and current.right.right is None:
                num_leaf += 1
                if num_leaf in identifiers:
                    current.right = None
            num_leaf = delete_leaves_by_id(bst_, identifiers, current.right, num_leaf, flag)
    return num_leaf

bst = BinarySearchTree()
rd.seed(1)
for _ in range(20):
    bst.insert(rd.randint(10,1000))
bst.print()
delete_leaves_by_id(bst,[1,3,4])
bst.print()
