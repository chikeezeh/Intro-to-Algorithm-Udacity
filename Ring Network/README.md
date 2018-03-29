## Ring Network

A ring network consist of vertices(nodes) that are connected to a neighboring vertex like a Chain Network.
The last vertex is then connected to the beginning vertex with a loop.

### Implementation
The ring structure is implemented as a dictionary of dictionaries.
The keys in the outer dictionary are the nodes, while the keys in the internal
dictionary shows the other nodes that the initial node is connected to.

### Example

0---1---2---3---4---0

We start at 0 and form a chain to the adjacent number which is 1, all the way to
4 then back to 0 to complete the ring.
This can be represented by a dictionary of dictionary as shown below:
{0: {1: '--', 4: '--'}, 1: {0: '--', 2: '--'}, 2: {1: '--', 3: '--'}, 3: {2: '--', 4: '--'}, 4: {0: '--', 3: '--'}}

The '--' shows the connection of a node to another node.
