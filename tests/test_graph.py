import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g = Graph(5)
        self.g.add_edge(0, 1, 2)
        self.g.add_edge(0, 2, 4)
        self.g.add_edge(1, 3, 2)
        self.g.add_edge(2, 3, 4)
        self.g.add_edge(2, 4, 3)
        self.g.add_edge(4, 3, -5)

    def test_bellman_ford(self):
        self.assertEqual(self.g.bellman_ford(0), [0, 2, 4, 2, 7])
