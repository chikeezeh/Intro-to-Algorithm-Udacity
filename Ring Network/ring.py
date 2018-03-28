def make_link(G, node1, node2):
    # the functions takes in a Graph and 2 nodes we want to connect.
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G
