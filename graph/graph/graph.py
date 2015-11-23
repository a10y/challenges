"""
Various algorithms around Bipartite graphs. Implementation in Python.
"""

class Node:
    def __init__(self, name):
        self.node_id = name

    def __hash__(self):
        return hash(self.node_id)

    def __eq__(self, other):
        return self.node_id == other.node_id

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __hash__(self):
        return hash((self.start, self.end))

class DirectedEdge(Edge):
    """Directed edge subtype of Edge. A DirectedEdge can only be "equal" to
    another DirectedEdge instance with the same start and endpoints.
    """
    def __eq__(self, other):
        return isinstance(other, DirectedEdge) and \
                self.start == other.start and self.end == other.end

class UndirectedEdge(Edge):
    """Undirected Edge subtype. An UndirectedEdge can only be "equal" to
    another UndirectedEdge that have the same start/endpointers (ignoring
    permutations).
    """
    def __eq__(self, other):
        return (self.start == other.start and self.end == other.end) \
                or (self.start == other.end and self.end == other.start)
    def __hash__(self):
        return hash((self.start, self.end))

class Graph:
    """Container class representing a full graph. Tracks all of the Nodes and
    Edges that make up the network.
    """
    def __init__(self):
        self.nodes = dict()
        self.edges = set()
        self.edges_for_node = dict()

    def add_node(self, n):
        if n.node_id in self.nodes:
            raise "Shit"
        self.nodes[n.node_id] = n

    def add_edge(self, e):
        self.edges.add(e)
        if e.start not in self.edges_for_node:
            self.edges_for_node[e.start] = []
        self.edges_for_node[e.start].append(e)
        if e.end not in self.edges_for_node:
            self.edges_for_node[e.end] = []
        self.edges_for_node[e.end].append(e)

    def edges_for(self, n):
        return self.edges_for_node[n]

