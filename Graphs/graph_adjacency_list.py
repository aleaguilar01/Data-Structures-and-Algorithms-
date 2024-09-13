class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []

    def add_edge(self, v1, v2):
        self.adjacencyList[v1].append(v2)
        self.adjacencyList[v2].append(v1)

    def remove_edge(self, v1, v2):
        self.adjacencyList[v1] = [x for x in self.adjacencyList[v1] if x != v2]
        self.adjacencyList[v2] = [x for x in self.adjacencyList[v2] if x != v1]

    def remove_vertex(self, v):
        for edge in self.adjacencyList[v]:
            self.remove_edge(v, edge)
        del self.adjacencyList[v]

    def deep_first_transversal_recursive(self, start):
        def dft(vertex):
            if not vertex:
                return
            result.append(vertex)
            visited_vertex[vertex] = True
            for neighbor in self.adjacencyList[vertex]:
                if neighbor not in visited_vertex:
                    dft(neighbor)

        result = []
        visited_vertex = {}
        dft(start)
        print(visited_vertex)

        return result

    def deep_first_iterative(self, start):
        result = []
        stack = [start]
        visited = {}

        while len(stack) > 0:
            current_vertex = stack.pop()
            result.append(current_vertex)
            visited[current_vertex] = True
            for neighbor in self.adjacencyList[current_vertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    stack.append(neighbor)
        return result

    def breadth_first_transversal(self, start):
        queue = [start]
        results = []
        visited = {}

        while len(queue) > 0:
            current_vertex = queue.pop(0)
            results.append(current_vertex)
            visited[current_vertex] = True
            for neighbor in self.adjacencyList[current_vertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return results




g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")

print(g.deep_first_transversal_recursive("A"))
print(g.deep_first_iterative("A"))
print(g.breadth_first_transversal("A"))