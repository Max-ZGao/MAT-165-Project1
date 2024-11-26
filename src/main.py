from PartitionGenerator import PartitionGenerator
from CrossingFreePartition import CrossingFreePartition
from Graph import GenerateMatrix
import numpy as np


points = np.array([]) # enter points here
k = 3




generator = PartitionGenerator(points)

partitions = []

while True:
    part = generator.next()

    if part == None:
        break
  
    partitions.append(part)

CFPartitions = CrossingFreePartition(partitions) # check which ones are crossing free

# output of the program. CFPartitions should be a list of lists of sets, such as [[{(1,1), (2,2)}, {(3,3)}], [{(1,1)},{(3,3), (2,2)}],[{(1,1),(3,3)},{(2,2)}]], where each sublists represents a partition and includes k crossing free sets. In this example, k = 3, so each sublists contains 3 sets
matrixGenerator = GenerateMatrix(CFPartitions)
matrix = matrixGenerator.getMatrix()
for row in matrix:
    print(row)