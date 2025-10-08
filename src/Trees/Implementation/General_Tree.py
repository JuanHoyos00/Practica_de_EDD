from typing import Any, Optional, Union


class GeneralNode:
    def __init__(self, value: Any):
        self.value: Any = value
        self.children: list[GeneralNode] = []
    def __repr__(self):
        return f"{self.value}"

class GeneralTree:
    def  __init__(self):
        self.root: Optional[GeneralNode] = None

    def search_node(self, value: Any, current: Optional[GeneralNode] = None, flag: bool = True) -> Union[GeneralNode,None,bool]:

        if flag:
            current = self.root

        if self.root is None:
            return False

        if current is None:
            return None

        if current.children:
            for child in current.children:
                if child.value == value:
                    return True

        for index in range(len(current.children)):
            self.search_node(value,current.children[index], False)

        if current.value == value:
            return current
        return False


    def add_child(self, node_: GeneralNode, child: Any) -> str:
        if self.search_node(node_):
            if isinstance(child,list):
                for node in child:
                    node_.children.append(GeneralNode(node))
            elif isinstance(child,tuple):
                for node in child:
                    node_.children.append(GeneralNode(node))
            else:
                node_.children.append(GeneralNode(child))
            return f'¡The node was added successfully.!'
        elif self.root is None:
            self.root = GeneralNode(child)
            return f'¡The node was added successfully.!'
        else:
            return f'¡The node does not exist.!'

    def print(self, node=None, prefix="", is_last=True, flag=True):
        if flag:
            node = self.root
        if not node:
            print("Empty Tree")
            return
        connector = "└── " if is_last else "├── "
        print(prefix + connector + str(node.value))
        new_prefix = prefix + ("    " if is_last else "│   ")
        for i, child in enumerate(node.children):
            is_child_last = i == len(node.children) - 1
            self.print(child, new_prefix, is_child_last, False)

