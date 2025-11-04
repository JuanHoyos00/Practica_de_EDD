from collections import deque
from typing import Any, Optional


class BinaryNode:

    def __init__(self, value: Any):
        self.value: Any = value
        self.right: Optional[BinaryNode] = None
        self.left: Optional[BinaryNode] = None

    def __repr__(self):
        return f'{self.value}'

class BinaryTree:

    def __init__(self):
        self.root: Optional[BinaryNode] = None

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

    def insert_by_level(self, values: list[Any]) -> Optional[str]:
        if not values:
            return None

        if self.root is not None:
            return 'Tree must be empty'

        self.root = BinaryNode(values.pop(0))
        queue = deque([self.root])

        while values:
            current = queue.popleft()

            if values:
                val = values.pop(0)
                if val is not None:
                    current.left = BinaryNode(val)
                    queue.append(current.left)

            if values:
                val = values.pop(0)
                if val is not None:
                    current.right = BinaryNode(val)
                    queue.append(current.right)

        return None

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

    def search(self,value: Any, current: None|BinaryNode = None, flag: bool = True) -> bool:

        if flag:
            current = self.root
            flag = False

        if current is None:
            return False

        if current.value == value:
            return True

        return self.search(value, current.left, flag) or self.search(value, current.right, flag)






