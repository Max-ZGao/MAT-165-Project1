
class Edge:

    def __init__(self, fr, to):
        self.from = fr
        self.to = to


class UndirectedGraph:

    def __init__(self):
        self.dict = {}
        self.vertices = []
        self.adjacency_matrix = {}
        return


    def has_vertex(vertex):
        return self.dict[vertex] != None


    
    def add_vertex(vertex):
        if not self.has_vertex(vertex):
            self.dict[vertex] = len(self.vertices)
            self.vertices.append(vertex)
    

    
    def is_connected(vertex1, vertex2):
        # TO DO
        
        return False
    
    def connect(vertex1, vertex2):

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # TO DO
        if not self.is_connected(vertex1, vertex2):
            return
        
        return
