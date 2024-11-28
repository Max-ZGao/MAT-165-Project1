from PartitionGenerator import PartitionGenerator
from CrossingFreePartition import CrossingFreePartition
from ConvexHull import ConvexHull
from Graph import GenerateMatrix
import numpy as np


points = [# enter points here
    [-10, -1],
    [10, -1],
    [0.5, 10], 
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
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