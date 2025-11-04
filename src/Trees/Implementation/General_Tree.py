from typing import Any, Optional


class GeneralNode:
    def __init__(self, value: Any):
        self.value: Any = value
        self.children: list[GeneralNode] = []

    def __repr__(self):
        return f'{self.value}'

class GeneralTree:
    def __init__(self):
        self.root: Optional[GeneralNode] = None

    def __repr__(self) -> str:

        if not self.root:
            return "🌱 Empty Tree"
        return self._build_tree_repr(self.root, "", True)

    def _build_tree_repr(self, node: GeneralNode, prefix: str, is_last: bool) -> str:
        tree_str = prefix + ("└── " if is_last else "├── ") + str(node.value) + "\n"
        prefix += "    " if is_last else "│   "

        child_count = len(node.children)
        for i, child in enumerate(node.children):
            is_last_child = (i == child_count - 1)
            tree_str += self._build_tree_repr(child, prefix, is_last_child)
        return tree_str

    def insert(self, parent: Any, value: Any, current: Optional[GeneralNode] = None, flag: bool = True) -> bool:
        if parent is None:
            self.root = GeneralNode(value)
            return True

        if self.root is None:
            self.root = GeneralNode(parent)
            self.root.children.append(GeneralNode(value))
            return True

        if flag:
            current = self.root
            flag = False

        if current.value == parent:
            current.children.append(GeneralNode(value))
            return True

        for i in range(len(current.children)):
            if self.insert(parent, value, current.children[i], flag):
                return True
        return False

    def delete(self, value: Any, current: Optional[GeneralNode] = None, flag: bool = True) -> bool:

        if flag:
            current = self.root
            flag = False

        for child in current.children:
            if child.value == value:
                pos: int = current.children.index(child)
                current.children.extend(current.children[pos].children)
                current.children.pop(pos)
                return True

        for child in current.children:
            self.delete(value, child, flag)

        return False









