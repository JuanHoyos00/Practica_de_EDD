from typing import Any, Optional
from src.Trees.Implementation.General_Tree import GeneralTree, GeneralNode

def delete_values(gt: GeneralTree, value: Any, current: Optional[GeneralNode] = None, flag: bool = True):
    if flag:
        current = gt.root
        flag = False
    i = 0
    for child in current.children:
        if child.value == value:
            current.children.extend(child.children)
            current.children.pop(i)
        i += 1

    for j in range(len(current.children)):
        delete_values(gt, value, current.children[j],flag)

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
delete_values(tree, 'B')
print(tree)
