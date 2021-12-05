from graph import Graph


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(0, 1, 8)
    g.add_edge(0, 2, 10)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 5, 2)
    g.add_edge(3, 5, -1)
    g.add_edge(3, 2, -4)
    g.add_edge(5, 4, -2)
    g.add_edge(4, 2, 1)

    g.bellman_ford(0)
