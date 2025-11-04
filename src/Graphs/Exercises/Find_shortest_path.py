from src.Graphs.Implementation.Weighted_Graph import WeightedGraph
from typing import Any, List
def find_shortest_path(wg: WeightedGraph, vertex_1: Any, vertex_2: Any, current_weight: int = 0, current_path: List[Any] = None, paths: tuple[int,list[Any]] = None) -> list[Any]|str:
    if paths is None:
        current_path = []
        paths = []
    if vertex_1 not in wg.adj_list or vertex_2 not in wg.adj_list:
        return paths
    if vertex_1 in current_path:
        return paths

    current_path.append(vertex_1)

    if vertex_1 == vertex_2:
        paths.append((current_weight,current_path.copy()))
        return paths

    for neighbor, weight in wg.adj_list[vertex_1]:
        find_shortest_path(wg, neighbor, vertex_2, current_weight + weight, current_path, paths)
        current_path.pop()

    return min(paths)






Wg = WeightedGraph()
Wg.add_edge('A', 'B', 111, )
Wg.add_edge('A', 'C',8,)
Wg.add_edge('C', 'B', 8,)


Wg.print_adj_matrix()
Wg.print_adj_list()
print(find_shortest_path(Wg,'A','B'))