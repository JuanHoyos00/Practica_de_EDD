from typing import Any, Optional, List
import random

class BinaryNode:

    def __init__(self, value: Any):
        self.value: Any = value
        self.right: Optional[BinaryNode] = None
        self.left: Optional[BinaryNode] = None

    def __repr__(self):
        return f'{self.value}'

class BinarySearchTree:
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

    def insert(self, value: Any, current: Optional[BinaryNode] = None) -> bool|None:

            if self.root is None:
                self.root = BinaryNode(value)
                return True

            if current is None:
                current = self.root

            if value < current.value:
                if current.left is None:
                    current.left = BinaryNode(value)
                    return True
                return self.insert(value, current.left)


            elif value > current.value:
                if current.right is None:
                    current.right = BinaryNode(value)
                    return True
                return self.insert(value, current.right)

            else:
                return False

    def search(self, value: Any, current: Optional[BinaryNode] = None, flag: bool = True):

        if flag:
            current = self.root
            flag = False

        if current is None:
            return False

        if current.value == value:
            return True

        if value < current.value:
            return self.search(value, current.left, flag)

        if value > current.value:
            return self.search(value, current.right, flag)

        return False

    def inorder(self, current: BinaryNode = None, flag: bool = True) -> None:
        if flag:
            current = self.root
            flag = False

        if current is None:
            return None
        # LEFT ROOT RIGHT
        self.inorder(current.left, flag)
        print(current.value)
        self.inorder(current.right, flag)

        return None

    def preorder(self, current: BinaryNode = None, flag: bool = True) -> None:
        if flag:
            current = self.root
            flag = False

        if current is None:
            return None

        # ROOT LEFT RIGHT
        print(current.value)
        self.preorder(current.left, flag)
        self.preorder(current.right, flag)

        return None

    def postorder(self, current: BinaryNode = None, flag: bool = True) -> None:
        if flag:
            current = self.root
            flag = False

        if current is None:
            return None

        # LEFT RIGHT ROOT
        self.postorder(current.left, flag)
        self.postorder(current.right, flag)
        print(current.value)

        return None

    def bfs(self) -> List[BinaryNode]:
        to_visit: List[BinaryNode] = [self.root]
        visited: List[BinaryNode] = []

        while to_visit:
            current = to_visit.pop(0)
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)

            visited.append(current)

        return visited

    def dfs(self, current = None, flag = True, visited = None):

        if visited is None:
            visited = []

        if flag:
            current = self.root

        if current is None:
            return visited

        visited.append(current.value)
        self.dfs(current.left, False, visited)
        self.dfs(current.right, False, visited)

        return visited
bst = BinarySearchTree()
random.seed(1)
for _ in range(10):
    n = random.randint(1,100)
    bst.insert(n)
