class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, value, priority):
        self.values.append({"value": value, "priority": priority})
        self.sort()

    def dequeue(self):
        return self.values.pop(0)

    def sort(self):
        self.values.sort(key=lambda x: x["priority"])

class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2, weight):
        self.adjacency_list[v1] = {"node": v2, "weight": weight}
        self.adjacency_list[v2] = {"node": v1, "weight": weight}

    def Dijkstra(self, start, finish):
        nodes = PriorityQueue()
        distances = {}
        previous = {}

        ##build up initial state
        for vertex in self.adjacency_list:
            if vertex == start:
                distances[vertex] = 0
                nodes.enqueue(vertex,0)
            else:
                distances[vertex] = float("inf")
                nodes.enqueue(vertex, float("inf"))

            previous[vertex] = None

        ##as long as there is something to visit

        while len(nodes.values) > 0:
            smallest = nodes.dequeue()




graph = WeightedGraph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")

graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "E", 3)
graph.add_edge("C", "D", 2)
graph.add_edge("C", "F", 4)
graph.add_edge("D", "E", 3)
graph.add_edge("D", "F", 1)
graph.add_edge("E", "F", 1)

graph.Dijkstra("A", "F")
