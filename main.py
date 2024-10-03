# Example adjacency matrix (unweighted)
adj_matrix = [[0, 1, 1, 0],
              [1, 0, 1, 1],
              [1, 1, 0, 1],
              [0, 1, 1, 0]]

# Number of nodes in the graph
num_nodes = len(adj_matrix)

# Translate the matrix to a graph (adjacency list)
graph = {}

for i in range(num_nodes):
    graph[i] = []
    for j in range(num_nodes):
        if adj_matrix[i][j] != 0:  # There's an edge
            graph[i].append(j)

# Display the graph as an adjacency list
for node, neighbors in graph.items():
    print(f"Node {node} is connected to: {', '.join(map(str, neighbors))}")
