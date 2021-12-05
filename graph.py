class Graph:
    def __init__(self, vertices):
        self.graph = []
        self.V = vertices

    def add_edge(self, start_vertex, end_vertex, edge_weight):
        self.graph.append([start_vertex, end_vertex, edge_weight])

    def print_solution(self, distance):

        print("Vertex Distance from Source")

        for i in range(self.V):
            print(f'{i} -> {distance[i]}')

    def bellman_ford(self, source_index):
        dist = [float('inf')] * self.V

        dist[source_index] = 0

        for i in range(self.V - 1):
            for start_vertex, end_vertex, edge_weight in self.graph:
                if dist[start_vertex] + edge_weight < dist[end_vertex]:
                    dist[end_vertex] = dist[start_vertex] + edge_weight

        for start_vertex, end_vertex, edge_weight in self.graph:
            if dist[start_vertex] + edge_weight < dist[end_vertex]:
                print("There is a negative weight cycle in graph")
                return False

        self.print_solution(dist)
        return dist
