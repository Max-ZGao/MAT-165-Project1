from PartitionGenerator import PartitionGenerator
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



graph = UndirectedGraph(partitions)

for part1 in partitions:
    for part2 in partitions:
        if part1.is_distance_1_from(part2):
            graph.connect(part1, part2)


