from PartitionGenerator import PartitionGenerator
from CrossingFreePartition import CrossingFreePartition
from ConvexHull import ConvexHull
from Graph import GenerateMatrix
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


points = [# enter points here
    [0,8],
    [1,8],
    [6,-4],
    [7,-3],
    [-9,-2]
]

k = 3




generator = PartitionGenerator(points, k)

partitions = []

print("Valid Partitions")
while True:
    part = generator.next()
    
    if part == None:
        break
  
    partitions.append(part)
    print(part)

print()
print("Matrix")
# output of the program. CFPartitions should be a list of lists of sets, such as [[{(1,1), (2,2)}, {(3,3)}], [{(1,1)},{(3,3), (2,2)}],[{(1,1),(3,3)},{(2,2)}]], where each sublists represents a partition and includes k crossing free sets. In this example, k = 3, so each sublists contains 3 sets
matrixGenerator = GenerateMatrix(partitions)
matrix = matrixGenerator.getMatrix()
for row in matrix:
    print(row)

print(matrix)
# Define the adjacency matrix
adj_matrix = np.array(matrix)

# Create the graph
G = nx.from_numpy_matrix(adj_matrix)

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # Use spring layout for better visualization
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=500)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')
plt.title("Grafo generado a partir de la matriz de adyacencia")
plt.show()