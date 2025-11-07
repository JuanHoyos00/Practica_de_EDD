from src.Trees.Implementation.General_Tree import GeneralTree
def branches_whit_unique_value(gt_: GeneralTree, current = None, branches: list[list[str]] = None, aux_list:list[str] = None, flag: bool = True):
    if branches is None:
        branches = []
        aux_list = []

    if flag:
        current = gt_.root
        flag = False

    aux_list.append(current.value)

    if not current.children:
        if len(aux_list) == len(set(aux_list)):
            branches.append([aux_list[0],aux_list[-1]])
            return branches
        return branches

    for i in range(len(current.children)):
        branches_whit_unique_value(gt, current.children[i], branches, aux_list,flag)
        aux_list.pop()
    return branches
gt = GeneralTree()
gt.insert('A','B')
gt.insert('A','C')
gt.insert('A','D')
gt.insert('A','E')
gt.insert('A','F')
gt.insert('A','G')
gt.insert('B','H')
gt.insert('B','I')
gt.insert('B','J')
gt.insert('C','C')
gt.insert('F','A')
gt.insert('G','F')
gt.insert('H','K')
gt.insert('K','B')
print(gt)
print(branches_whit_unique_value(gt))