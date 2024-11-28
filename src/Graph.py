class GenerateMatrix:
    def __init__(self, partitions):
        self.partitions = partitions
    
    def getMatrix(self):
        partitions = self.partitions
        n = len(partitions)
        matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)] # identity matrix
        for i in range(n):
            for j in range(i+1, n):
                if self.distance_is_one(partitions[i], partitions[j]):
                    matrix[i][j] = 1
                    matrix[j][i] = 1
        return matrix
    
    def distance_is_one(self, partitionSet1, partitionSet2):
        # convert list of sets to list of lists
        partitionList1 = []
        for set in partitionSet1:
            partitionList1.append(list(set)) # convert each sets to list
        partitionList2 = []
        for set in partitionSet2:
            partitionList2.append(list(set)) # convert each sets to list
        
        # if elements are missing, there is a problem. Check crossingFreePartition.py
        element1 = []
        for lst in partitionList1:
            for sublist in lst:
                element1.append(sublist)
        element2 = []
        for lst in partitionList2:
            for sublist in lst:
                element2.append(sublist)
        
        element1.sort()
        element2.sort()
        if element1 != element2:
            raise Exception("Crossing-free partition is done incorrectly. Check CrossingFreePartition.py.")
        
        # identify subsets that are different
        unmatched1 = []
        unmatched2 = []
        for s1 in partitionList1:
            if s1 not in partitionList2:
                unmatched1.append(s1)
        for s2 in partitionList2:
            if s2 not in partitionList1:
                unmatched2.append(s2)

        # check if only two subsets differ
        if len(unmatched1) != 2 or len(unmatched2) != 2:
            return False
        
        # check if moving one element can make the unmatched sets match
        s1a, s1b = unmatched1
        s2a, s2b = unmatched2
        
        # assumes the order of unmatched1 and unmatched2 is the same
        for point in s1a:
            s1aCopy = s1a[:]
            s1aCopy.remove(point)
            s1bCopy = s1b[:]
            s1bCopy.append(point)
            if s1aCopy == s2a and s1bCopy == s2b: return True
        for point in s1b:
            s1aCopy = s1a[:]
            s1aCopy.append(point)
            s1bCopy = s1b[:]
            s1bCopy.remove(point)
            if s1bCopy == s2b and s1aCopy == s2a: return True
        
        return False

# test case and usage 
if __name__ == '__main__':
    patitions = [[{(1,1), (2,2)}, {(3,3)}], [{(1,1)},{(3,3), (2,2)}],[{(1,1),(3,3)},{(2,2)}]]
    matrixGenerator = GenerateMatrix(patitions)
    matrix = matrixGenerator.getMatrix()
    for row in matrix:
        print(row)