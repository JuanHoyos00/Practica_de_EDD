from src.Trees.Implementation.Binary_Tree import BinaryTree
def tjognntrj(bt):
    def hdhd(bt, current = None, current_path = [], paths = [], flag = True):
        if flag:
            current = bt.root
            flag = False

        if current is None:
            return paths

        current_path.append(current.value)

        if current.right is None and current.left is None:
            paths.append(current_path.copy())
            return paths


        hdhd(bt, current.left, current_path, paths, flag)
        current_path.pop()
        hdhd(bt, current.right, current_path, paths, flag)
        current_path.pop()
        print(paths, 'k')
        return max(paths, key=lambda x: len(x))


    paths = hdhd(bt)
    print(paths)

    pos = 1
    current = bt.root
    while pos < len(paths):
        if current.left.value == paths[pos]:
            current = current.left
            pos += 1
        elif current.right.value == paths[pos]:
            current = current.right
            pos += 1
    return bt
bt = BinaryTree()
bt.insert_parent_child(5, 4)
bt.insert_parent_child(5, 2)
bt.insert_parent_child(4, 7)
bt.insert_parent_child(7, 9)
bt.insert_parent_child(7, 8)
bt.insert_parent_child(2, 19)
bt.insert_parent_child(2, 11)
bt.insert_parent_child(19, 10)




bt.print()
tjognntrj(bt)