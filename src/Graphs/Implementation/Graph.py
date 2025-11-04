from typing import Any, List, Dict, Optional


class Graph:

    def __init__(self):
        self.adj_matrix: List[List[int]] = []
        self.nodes: List[Any] = []
        self.adj_list: Dict[Any, List[Any]] = {}
        self.size: int = 0

    def print_adj_matrix(self):
        i = 0
        str_ = ''
        for row in self.adj_matrix:
            print(f'[{self.nodes[i]}]-{row}')
            i+=1
        for j in self.nodes:
            str_ += f'{j}, '
        if len(str_) >= 2:
            str_ = str_[:-2]
            print(f'    [{str_}]')

    def print_adj_list(self):
        for vertex,neighbors in self.adj_list.items():
            print(f'{vertex} -> {neighbors}')

    def add_vertex(self,value: Any):
        if value not in self.nodes:
            self.size += 1
            self.nodes.append(value)
            self.adj_list[value] = []
            for row in self.adj_matrix:
                row.append(0)
            self.adj_matrix.append([0] * self.size)

    def add_edge(self, vertex_1: Any, vertex_2: Any, directed: bool = True):
        if vertex_1 not in self.nodes:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.nodes:
            self.add_vertex(vertex_2)

        pos_v1: int = self.nodes.index(vertex_1)
        pos_v2: int = self.nodes.index(vertex_2)

        if vertex_2 not in self.adj_list[vertex_1]:
            self.adj_matrix[pos_v1][pos_v2] = 1
            self.adj_list[vertex_1].append(vertex_2)
        if not directed and vertex_1 not in self.adj_list[vertex_2]:
            self.adj_matrix[pos_v2][pos_v1] = 1
            self.adj_list[vertex_2].append(vertex_1)

    def dfs(self, start_vertex: Any, adj_matrix: bool = True, visited: Optional[list[Any]] = None, flag: bool = True) -> List[Any]:
        if flag:
            visited = []
            flag = False
        if adj_matrix:
            if start_vertex in self.nodes:
                visited.append(start_vertex)
                pos = self.nodes.index(start_vertex)
                for i, neighbor in enumerate(self.adj_matrix[pos]):
                    if neighbor == 1 and self.nodes[i] not in visited:
                        self.dfs(self.nodes[i], adj_matrix, visited, flag)
                    i += 1
                return visited
            else:
                return []
        else:
            if start_vertex in self.adj_list:
                visited.append(start_vertex)
                for neighbor in self.adj_list[start_vertex]:
                    if neighbor not in visited:
                        self.dfs(neighbor, adj_matrix, visited, flag)
                return visited
            else:
                return visited

    def bfs(self, start_vertex: Any, adj_matrix: bool = True, visited: Optional[List[Any]] = None, to_visit: Optional[List[Any]] = None, flag: bool = True) -> List[Any]:
        if flag:
            visited = []
            to_visit = []
            flag = False
        if adj_matrix:
            if start_vertex in self.nodes and start_vertex not in visited:
                visited.append(start_vertex)
            pos = self.nodes.index(start_vertex)
            for i,neighbor in enumerate(self.adj_matrix[pos]):
                if neighbor == 1 and self.nodes[i] not in to_visit and self.nodes[i] not in visited:
                    to_visit.append(self.nodes[i])
            if to_visit:
                self.bfs(to_visit.pop(0),adj_matrix, visited, to_visit, flag)
        else:
            if start_vertex in self.adj_list and start_vertex not in visited:
                visited.append(start_vertex)
            for neighbor in self.adj_list[start_vertex]:
                if neighbor not in to_visit and neighbor not in visited:
                    to_visit.append(neighbor)
            if to_visit:
                self.bfs(to_visit.pop(0),adj_matrix, visited, to_visit, flag)
        return visited