from PartitionGenerator import PartitionGenerator
from CrossingFreePartition import CrossingFreePartition
from ConvexHull import ConvexHull
from Graph import GenerateMatrix
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# You can input either 2D or 3D points here
points = [
    # For 2D points, use format [x, y]
   
    
    # For 3D points, use format [x, y, z]
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]

# Number of partitions
k = 3

# Create partition generator
generator = PartitionGenerator(points, k)

# Store valid partitions
partitions = []

# Get all valid partitions
print("Valid Partitions:")
while True:
    part = generator.next()
    if part == None:
        break
    partitions.append(part)
    print(part)

# Generate adjacency matrix
print("\nAdjacency Matrix:")
matrixGenerator = GenerateMatrix(partitions)
matrix = matrixGenerator.getMatrix()
for row in matrix:
    print(row)

# Create graph visualization
G = nx.Graph()

# Add nodes
for i in range(len(matrix)):
    G.add_node(i)

# Add edges
for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        if matrix[i][j] == 1:
            G.add_edge(i, j)

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', 
        node_size=500, font_size=16, font_weight='bold')
plt.title("Partition Adjacency Graph")
plt.show()