class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2, weight):
        self.adjacency_list[v1] = {"node": v2, "weight": weight}
        self.adjacency_list[v2] = {"node": v1, "weight": weight}


