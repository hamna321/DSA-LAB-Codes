class GraphAdjMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1 

    def display(self):
        for row in self.adj_matrix:
            print(row)
graph_matrix = GraphAdjMatrix(5)
graph_matrix.add_edge(0, 1)
graph_matrix.add_edge(0, 2)
graph_matrix.add_edge(1, 3)
graph_matrix.add_edge(2, 4)
print("Adjacency Matrix:")
graph_matrix.display()
