from CrossingFreePartition import CrossingFreePartition
import numpy as np

class PartitionGenerator:
    """
    This class generates all possible ways to divide a set of objects into smaller groups (partitions),
    where each partition must follow certain rules about not intersecting.
    Think of it like dividing students into study groups where no group's workspace can overlap with another.
    """
    
    def __init__(self, objects, k):
        """
        Sets up our partition generator with:
        - objects: the things we want to divide into groups (like students)
        - k: maximum number of groups we can create
        
        For example, if we have students A,B,C and k=2, we can only make up to 2 groups,
        like [A,B][C] or [A][B,C], but not [A][B][C] because that's 3 groups.
        """
        self.objects = objects              # Store our list of objects to partition
        self.k = k                          # Maximum number of groups allowed
        self.current_partition_index = 0     # Keep track of which partition we're on
        self.all_partitions = []            # Will store all valid ways to divide our objects
        self._generate_all_partitions(objects)  # Create all possible valid partitions

    def _generate_all_partitions(self, objects):
        """
        This is where the magic happens! We try all possible ways to divide our objects.
        We use a technique called "backtracking" - imagine filling in a puzzle
        and if we make a mistake, we go back and try a different way.
        """
        
        def backtrack(remaining_objects, current_partition):
            """
            This helper function tries different ways to add objects to groups.
            It's like having a box of objects and deciding for each one:
            1. Should it go in an existing group?
            2. Should it start a new group?
            
            remaining_objects: objects we haven't put in groups yet
            current_partition: the groups we've made so far
            """
            
            # If we've used all objects, check if this grouping is valid
            if not remaining_objects:
                if len(current_partition) <= self.k:  # Make sure we didn't make too many groups
                    # Convert our groups to the format needed for checking validity
                    np_partition = [np.array(subset) for subset in current_partition]
                    # Check if this grouping follows our rules (no intersecting groups)
                    cfp = CrossingFreePartition(np_partition)
                    if cfp.is_valid:
                        self.all_partitions.append(np_partition)  # Save this valid grouping
                return

            # Take the next object we need to place
            obj = remaining_objects[0]
            # Keep track of the other objects we still need to place
            new_remaining = remaining_objects[1:]

            # Try option 1: Add the object to each existing group
            for i in range(len(current_partition)):
                # Make a copy so we don't modify the original groups
                new_partition = [subset.copy() for subset in current_partition]
                new_partition[i].append(obj)  # Add object to this group
                # Recursively continue with remaining objects
                backtrack(new_remaining, new_partition)

            # Try option 2: Create a new group (if we haven't hit our group limit)
            if len(current_partition) < self.k:
                # Create a new group with just this object
                new_partition = current_partition + [[obj]]
                # Recursively continue with remaining objects
                backtrack(new_remaining, new_partition)

        # Start by putting the first object in its own group
        backtrack(objects[1:], [[objects[0]]])

    def next(self):
        """
        Returns the next valid partition we found.
        Like dealing cards one at a time, this gives you the next valid grouping.
        Returns None when we've shown all possible groupings.
        """
        if self.current_partition_index >= len(self.all_partitions):
            return None  # We've shown all partitions
            
        partition = self.all_partitions[self.current_partition_index]
        self.current_partition_index += 1  # Move to next partition
        return partition

    def reset(self):
        """
        Starts over from the beginning.
        Like reshuffling the deck to start dealing cards again.
        """
        self.current_partition_index = 0

    def get_all_partitions(self):
        """
        Returns all valid partitions at once.
        Instead of dealing cards one at a time, this shows the whole deck.
        """
        return self.all_partitions

    def count_partitions(self):
        """
        Tells us how many valid ways we found to divide the objects.
        Like counting how many different possible hands we could deal.
        """
        return len(self.all_partitions)

    def has_next(self):
        """
        Checks if there are more partitions to show.
        Like checking if there are more cards to deal.
        """
        return self.current_partition_index < len(self.all_partitions)

