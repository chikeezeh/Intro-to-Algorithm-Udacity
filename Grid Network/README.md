## Grid Network

A Grid network consist of vertices(nodes) that are connected in the form of a rectangular
grid.

### Implementation
The Grid network is also implemented as a dictionary of dictionary, with the outer
key as the main nodes, and the inner keys showing the nodes that are interconnected.

### Example
```
0---1---2
|   |   |
7---8---3
|   |   |
6---5---4
```
The above is a 9 node grid.
The number of edges for a square grid, i.e n = perfect square;
```
E = 2*sqrt(n)*(sqrt(n)-1)
```
