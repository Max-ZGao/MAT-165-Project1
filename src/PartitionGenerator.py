# We need CrossingFreePartition to check if our partitions are valid
# (if their convex hulls don't intersect)
from CrossingFreePartition import CrossingFreePartition
# numpy helps us work with arrays and mathematical operations
import numpy as np

class PartitionGenerator:
    def __init__(self, objects, k):
        """
        This is where we set up our partition generator.
        Think of it like setting up a card dealer before dealing cards.
        
        objects: These are the points we want to divide into groups
                (like having a deck of cards to deal)
        k: This tells us exactly how many groups we need to make
           (like dealing cards to exactly k players)
        """
        # Store the objects (points) we'll be partitioning
        self.objects = objects
        # Store how many groups we need to make
        self.k = k
        # Keep track of which partition we're currently looking at
        # (like keeping track of which hand of cards we're dealing)
        self.current_partition_index = 0
        # This will store all the valid ways we can divide our points
        # (like keeping track of all possible ways to deal the cards)
        self.all_partitions = []
        # Start generating all possible partitions
        self._generate_all_partitions(objects)

    def _is_duplicate_partition(self, new_partition):
        """
        Check if this partition is already in our list
        Two partitions are the same if they have the same groups, even in different order
        Like checking if we've already dealt the cards this way before
        """
        # Convert the new partition to sets for easier comparison
        new_partition_sets = [set(tuple(map(tuple, subset)) for subset in new_partition)]
        
        # Check against all existing partitions
        for existing_partition in self.all_partitions:
            # Convert existing partition to sets
            existing_partition_sets = [set(tuple(map(tuple, subset)) for subset in existing_partition)]
            
            # If they have the same groups (even in different order), it's a duplicate
            if len(new_partition_sets) == len(existing_partition_sets):
                matches = 0
                for new_set in new_partition_sets:
                    if any(new_set == existing_set for existing_set in existing_partition_sets):
                        matches += 1
                if matches == len(new_partition_sets):
                    return True
        return False

    def _generate_all_partitions(self, objects):
        # This helper function (backtrack) tries different ways to group the points
        def backtrack(remaining_objects, current_partition):
            # If we've used all our objects (dealt all cards)...
            if not remaining_objects:
                # Check if we have exactly k groups (k players got cards)
                if len(current_partition) == self.k:
                    # Convert the partition to numpy arrays
                    np_partition = [np.array(subset) for subset in current_partition]
                    # Only add if it's not a duplicate
                    if not self._is_duplicate_partition(np_partition):
                        self.all_partitions.append(np_partition)
                return

            # Take the next object to place (like picking up the next card)
            obj = remaining_objects[0]
            # Keep track of remaining objects (remaining cards in deck)
            new_remaining = remaining_objects[1:]

            # Try adding to existing groups (giving card to existing players)
            for i in range(len(current_partition)):
                # Make a copy so we don't mess up our current arrangement
                new_partition = [subset.copy() for subset in current_partition]
                # Add object to this group (give card to this player)
                new_partition[i].append(obj)
                # Try dealing rest of the cards this way
                backtrack(new_remaining, new_partition)

            # Try creating a new group (adding a new player)
            # but only if we haven't reached k groups yet
            if len(current_partition) < self.k:
                # Create new group with just this object
                # (give card to new player)
                new_partition = current_partition + [[obj]]
                # Try dealing rest of the cards this way
                backtrack(new_remaining, new_partition)

        # Only start if we have enough objects to make k groups
        # (need at least k cards to deal to k players)
        if len(objects) >= self.k:
            # Start by putting first object in its own group
            # (give first card to first player)
            backtrack(objects[1:], [[objects[0]]])

    # [Rest of the methods remain the same]
    def next(self):
        """
        Get the next valid partition, like dealing the next hand of cards
        Returns None if we've shown all possible ways to deal
        """
        if self.current_partition_index >= len(self.all_partitions):
            return None
        partition = self.all_partitions[self.current_partition_index]
        self.current_partition_index += 1
        return partition

    def reset(self):
        """
        Start over from the beginning
        Like gathering all cards and starting to deal again
        """
        self.current_partition_index = 0

    def get_all_partitions(self):
        """
        Show all possible ways to divide the objects
        Like showing all possible ways the cards could be dealt
        """
        return self.all_partitions

    def count_partitions(self):
        """
        Count how many different ways we can divide the objects
        Like counting how many different possible deals there are
        """
        return len(self.all_partitions)

    def has_next(self):
        """
        Check if there are more partitions to show
        Like checking if there are more possible ways to deal
        """
        return self.current_partition_index < len(self.all_partitions)