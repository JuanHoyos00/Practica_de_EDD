from typing import Any, Optional
from src.Trees.Implementation.General_Tree import GeneralTree, GeneralNode

def change_values(gt: GeneralTree, value: Any, current: Optional[GeneralNode] = None, flag: bool = True) -> None:
    if flag:
        current = gt.root
        flag = False

    if current.value == value:
        for node in current.children:
            node.value = value
        return None

    for i in range(len(current.children)):
        change_values(gt, value, current.children[i], flag)
    return None
tree = GeneralTree()
tree.insert(None, "A")
tree.insert("A", "B")
tree.insert("A", "C")
tree.insert("B", "D")
tree.insert("B", "E")
tree.insert("C", "F")
tree.insert("E", "G")
tree.insert("E", "H")
tree.insert("B", "B")
tree.insert("B", "X")
tree.root.children[0].children[3].children.extend(list(map(GeneralNode, list("AYMUCHACHOS"))))
print(tree)
change_values(tree,'X')
print(tree)



