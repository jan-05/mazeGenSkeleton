# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.

# _author_ = 'Jeffrey Chan', <YOU>
# _copyright_ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


# from typing import List

# from maze.util import Coordinates
# from maze.graph import Graph


# class AdjMatGraph(Graph):
#     """
#     Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
#     to see what each of the overriden methods are meant to do.
#     """

#     def _init_(self):
#         ### Implement me! ###
#         pass



#     def addVertex(self, label:Coordinates):
#         ### Implement me! ###
#         pass



#     def addVertices(self, vertLabels:List[Coordinates]):
#         ### Implement me! ###
#         pass



#     def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
#         ### Implement me! ###
#         # remember to return booleans
#         pass        
    


#     def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
#         ### Implement me! ###
#         # remember to return booleans
#         pass



#     def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
#         ### Implement me! ###
#         # remember to return booleans
#         pass
        


#     def hasVertex(self, label:Coordinates)->bool:
#         ### Implement me! ###
#         # remember to return booleans
#         pass



#     def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
#         ### Implement me! ###
#         # remember to return booleans
#         pass



#     def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
#         ### Implement me! ###
#         # remember to return booleans
#         pass



#     def neighbours(self, label:Coordinates)->List[Coordinates]:
#         ### Implement me! ###
#         # remember to return list of coordinates
#         pass
from typing import List
from maze.util import Coordinates
from maze.graph import Graph

class AdjMatGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.vertices = {}  # Dictionary to store vertices
        self.adj_matrix = {}  # Adjacency matrix

    def addVertex(self, label: Coordinates):
        if label not in self.vertices:
            self.vertices[label] = len(self.vertices)  # Assigning index to vertex
            self.adj_matrix[label] = [False] * len(self.vertices)  # Initializing row
            for vertex in self.adj_matrix:
                vertex_index = self.vertices[vertex]
                self.adj_matrix[vertex].append(False)  # Adding new column
            return True
        return False

    def addVertices(self, vertLabels: List[Coordinates]):
        added = False
        for label in vertLabels:
            added = self.addVertex(label) or added
        return added

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            index1, index2 = self.vertices[vert1], self.vertices[vert2]
            self.adj_matrix[vert1][index2] = True
            self.adj_matrix[vert2][index1] = True
            return True
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            index1, index2 = self.vertices[vert1], self.vertices[vert2]
            self.adj_matrix[vert1][index2] = wallStatus
            self.adj_matrix[vert2][index1] = wallStatus
            return True
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        return self.updateWall(vert1, vert2, False)

    def hasVertex(self, label: Coordinates) -> bool:
        return label in self.vertices

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            index1, index2 = self.vertices[vert1], self.vertices[vert2]
            return self.adj_matrix[vert1][index2]
        return False

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            index1, index2 = self.vertices[vert1], self.vertices[vert2]
            return self.adj_matrix[vert1][index2]
        return False

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        if label in self.vertices:
            neighbours = []
            index = self.vertices[label]
            for vertex in self.adj_matrix:
                if self.adj_matrix[vertex][index]:
                    neighbours.append(vertex)
            return neighbours
        return []