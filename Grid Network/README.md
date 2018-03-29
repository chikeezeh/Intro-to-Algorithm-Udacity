## Grid Network

A Grid network consist of vertices(nodes) that are connected in the form of a rectangular
grid.

### Implementation


### Example

0---1
|   |
3---2

We start at 0 and form a chain to the adjacent number which is 1, all the way to
4 then back to 0 to complete the ring.
This can be represented by a dictionary of dictionary as shown below:
{0: {1: '--', 4: '--'}, 1: {0: '--', 2: '--'}, 2: {1: '--', 3: '--'}, 3: {2: '--', 4: '--'}, 4: {0: '--', 3: '--'}}

The '--' shows the connection of a node to another node
