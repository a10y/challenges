from graph.graph import UndirectedEdge, Graph, Node
from algorithms import is_bipartite
import unittest

class TestBipartiteDetectionCorrect(unittest.TestCase):
    def setUp(self):
        self.network = self.construct_bp_network()

    def runTest(self):
        self.assertTrue(is_bipartite(self.network))

    def construct_bp_network(self):
        network = Graph()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)

        # Add nodes to graph
        network.add_node(n1)
        network.add_node(n2)
        network.add_node(n3)
        network.add_node(n4)
        network.add_node(n5)
        network.add_node(n6)

        # Add edges in zig-zag pattern
        network.add_edge(UndirectedEdge(n1, n2))
        network.add_edge(UndirectedEdge(n2, n3))
        network.add_edge(UndirectedEdge(n3, n4))
        network.add_edge(UndirectedEdge(n4, n5))
        network.add_edge(UndirectedEdge(n5, n6))

        return network

class TestBipartiteDetectionIncorrect(unittest.TestCase):
    def setUp(self):
        self.network = self.construct_triangle_network()

    def test_nonbipartite(self):
        self.assertFalse(is_bipartite(self.network))

    def construct_triangle_network(self):
        """Constructs a triangle, clearly not bipartite"""
        network = Graph()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)

        network.add_node(n1)
        network.add_node(n2)
        network.add_node(n3)

        network.add_edge(UndirectedEdge(n1, n2))
        network.add_edge(UndirectedEdge(n2, n3))
        network.add_edge(UndirectedEdge(n3, n1))

        return network


if __name__ == '__main__':
    unittest.main()
