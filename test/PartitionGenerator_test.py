import numpy as np

class Point:
    def __init__(self, coords):
        self.coords = np.array(coords)
        self.dimension = len(coords)
        
    def __str__(self):
        return str(self.coords)
        
    def __array__(self):
        """Make Point compatible with np.array"""
        return self.coords
        
    def __iter__(self):
        """Make Point iterable"""
        return iter(self.coords)
        
    def __getitem__(self, key):
        """Allow indexing of Point"""
        return self.coords[key]

class PartitionGenerator:
    def __init__(self, objects, k):
        self.objects = objects
        self.k = k
        self.current_partition_index = 0
        self.all_partitions = []
        self._generate_all_partitions(objects)

    def _is_duplicate_partition(self, new_partition):
        # Convert points to tuples for comparison
        def partition_to_sets(partition):
            return frozenset(
                frozenset(tuple(point.coords) for point in subset)
                for subset in partition
            )
        
        new_partition_set = partition_to_sets(new_partition)
        return any(new_partition_set == partition_to_sets(existing) 
                  for existing in self.all_partitions)

    def _generate_all_partitions(self, objects):
        def backtrack(remaining_objects, current_partition):
            if not remaining_objects:
                if len(current_partition) == self.k:
                    # Store points directly instead of converting to np.array
                    if not self._is_duplicate_partition(current_partition):
                        self.all_partitions.append([subset.copy() for subset in current_partition])
                return

            obj = remaining_objects[0]
            new_remaining = remaining_objects[1:]

            # Try adding to existing subsets
            for i in range(len(current_partition)):
                new_partition = [subset.copy() for subset in current_partition]
                new_partition[i].append(obj)
                backtrack(new_remaining, new_partition)

            # Try creating new subset if we haven't reached k subsets
            if len(current_partition) < self.k:
                new_partition = current_partition + [[obj]]
                backtrack(new_remaining, new_partition)

        if len(objects) >= self.k:
            backtrack(objects[1:], [[objects[0]]])

    def next(self):
        if self.current_partition_index >= len(self.all_partitions):
            return None
        partition = self.all_partitions[self.current_partition_index]
        self.current_partition_index += 1
        return partition

    def reset(self):
        self.current_partition_index = 0

    def get_all_partitions(self):
        return self.all_partitions

    def count_partitions(self):
        return len(self.all_partitions)

    def has_next(self):
        return self.current_partition_index < len(self.all_partitions)

def print_test_results(test_name, points, k):
    print(f"\n=== {test_name} ===")
    print("Input points:", [str(p) for p in points])
    print(f"Testing with exactly k={k} partitions:")
    
    generator = PartitionGenerator(points, k=k)
    partition_count = 0
    
    while True:
        partition = generator.next()
        if partition is None:
            break
        partition_count += 1
        print(f"\nPartition {partition_count}:")
        for subset in partition:
            print("  Subset:", [str(p) for p in subset])
            
    print(f"\nTotal partitions found: {partition_count}")
    return partition_count

def test_simple_cases():
    # Simple test with three points
    print("\nTesting simple cases:")
    points = [
        Point([0, 0]),
        Point([1, 0]),
        Point([0, 1])
    ]
    
    print("\nTesting k=2:")
    print_test_results("Three points", points, k=2)
    
    print("\nTesting k=3:")
    print_test_results("Three points", points, k=3)

def test_square():
    # Test with four points in a square
    points = [
        Point([0, 0]),
        Point([1, 0]),
        Point([0, 1]),
        Point([1, 1])
    ]
    
    print("\nTesting square configuration:")
    print_test_results("Four points square", points, k=2)
    print_test_results("Four points square", points, k=3)

if __name__ == "__main__":
    test_simple_cases()
    test_square()