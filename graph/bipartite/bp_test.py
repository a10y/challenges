from ..graph.graph import UndirectedEdge, Graph, Node
from .algorithms import is_bipartite

def construct_bp_network():
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

def construct_triangle_network():
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


def test():
    network = construct_bp_network()
    is_bp = is_bipartite(network)
    print('Is bipartite (True): {}'.format(is_bp))
    network2 = construct_triangle_network()
    is_bp2 = is_bipartite(network2)
    print('Is bipartite (False): {}'.format(is_bp2))


if __name__ == '__main__':
    test()
