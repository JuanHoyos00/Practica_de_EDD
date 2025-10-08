from typing import Any, Optional


class BinaryNode:
    def __init__(self, value: Any):
        self.value: Any = value
        self.right: Optional[BinaryNode] = None
        self.left: Optional[BinaryNode] = None

class BinaryTree:
    def __init__(self):
        self.root: Optional[BinaryNode] = None

    def insert_parent_child(self, parent: Any, child: Any, current: Optional[BinaryNode] = None, flag: bool = True) -> bool:

        if flag:
            current = self.root

        if self.root is None:
            self.root = BinaryNode(parent)
            self.root.left = BinaryNode(child)
            return True

        if current is None:
            return False

        if current.value == parent:
            if current.left is None:
                current.left = BinaryNode(child)
                return True

            if current.right is None:
                current.right = BinaryNode(child)
                return True

        if self.insert_parent_child(parent, child, current.left, False):
            return True

        if self.insert_parent_child(parent, child, current.right, False):
            return True

        return False
    def print(self, node=None, prefix="", is_left=True, flag=True):
        if flag:
            node = self.root
        if not node:
            print("Empty Tree")
            return
        if node.right:
            self.print(node.right, prefix + ("│   " if is_left else "    "), False, False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left:
            self.print(node.left, prefix + ("    " if is_left else "│   "), True, False)

bt = BinaryTree()
bt.insert_parent_child(5,4)


bt.print()



