from graph.graph import Node, Edge, Graph
from queue import Queue

def is_bipartite(network):
    """Determines if a given network is bipartite
    High-level algorithm:
    * Perform BFS on the graph from an arbitrary node,
      storing the hop count from the start in each queue entry.
    * If we ever encounter a node a second time that has a different
      parity, the graph is non-bipartite
    """
    q = Queue()
    sides = dict()
    visited = set()

    # The empty network is trivially bipartite
    if len(network.nodes) == 0:
        return True

    # Choose aribtrary node to start with (first node here)
    start_node = network.nodes[list(network.nodes)[0]]
    q.put((0, start_node))
    sides[start_node] = 1

    while not q.empty():
        hop, node = q.get()
        if node in visited:
            if sides[node] is not hop % 2:
                return False
            else:
                continue
        visited.add(node)
        sides[node] = hop % 2
        for e in network.edges_for(node):
            other = e.start if e.end == node else e.end
            q.put((hop + 1, other))

    # If we've exhausted the list, return true
    return True

