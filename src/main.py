from PartitionGenerator import PartitionGenerator
from CrossingFreePartition import CrossingFreePartition
from Graph import UndirectedGraph
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



matrix = UndirectedGraph(CFPartitions)

print(matrix)