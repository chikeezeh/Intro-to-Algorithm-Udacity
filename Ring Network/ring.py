def make_link(G, node1, node2):
    # the functions takes in a Graph and 2 nodes we want to connect.
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = '--'
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = '--'
    return G


# make an empty graph
a_ring = {}

n = 5

# Add in the edges
for i in range(n):
    make_link(a_ring, i, (i + 1) % n)
print (a_ring)
