from collections import defaultdict

class GraphAdjList:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) 

    def display(self):
        for vertex, edges in self.adj_list.items():
            print(vertex, "->", " -> ".join(map(str, edges)))
graph_list = GraphAdjList()
graph_list.add_edge(0, 1)
graph_list.add_edge(0, 2)
graph_list.add_edge(1, 3)
graph_list.add_edge(2, 4)
print("\nAdjacency List:")
graph_list.display()
