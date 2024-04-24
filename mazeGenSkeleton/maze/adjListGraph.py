# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.

# _author_ = 'Jeffrey Chan', <YOU>
# _copyright_ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------

# class AdjListGraph(Graph):
#     """
#     Represents an undirected graph. Please complete the implementations of each method.
#     """

#     def _init_(self):
#         # Initialize an empty dictionary to store vertices and their neighbors
#         self.adj_list = {}

#     def addVertex(self, label: Coordinates):
#         # Add a new vertex to the graph
#         self.adj_list[label] = []

#     def addVertices(self, vertLabels: List[Coordinates]):
#         # Add multiple vertices to the graph
#         for label in vertLabels:
#             self.addVertex(label)

#     def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
#         # Add an edge between two vertices
#         if vert1 not in self.adj_list or vert2 not in self.adj_list:
#             return False

#         # Check if the edge already exists
#         if vert2 not in self.adj_list[vert1]:
#             # Add the edge
#             self.adj_list[vert1].append(vert2)
#             self.adj_list[vert2].append(vert1)  # Undirected graph
#             return True

#         return False

#     def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
#         # Update wall status between two vertices
#         if vert1 not in self.adj_list or vert2 not in self.adj_list:
#             return False
#         if vert2 in self.adj_list[vert1]:
#             # If edge exists, update wall status
#             self.adj_list[vert1].remove(vert2)
#             self.adj_list[vert2].remove(vert1)
#             return True
#         return False

#     def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
#         # Remove an edge between two vertices
#         if vert1 not in self.adj_list or vert2 not in self.adj_list:
#             return False
#         if vert2 in self.adj_list[vert1]:
#             self.adj_list[vert1].remove(vert2)
#             self.adj_list[vert2].remove(vert1)
#             return True
#         return False

#     def hasVertex(self, label: Coordinates) -> bool:
#         # Check if a vertex exists in the graph
#         return label in self.adj_list

#     def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
#         # Check if an edge exists between two vertices
#         if vert1 not in self.adj_list or vert2 not in self.adj_list:
#             return False
#         return vert2 in self.adj_list[vert1]

#     def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
#         # Get wall status between two vertices
#         return not self.hasEdge(vert1, vert2)

#     def neighbours(self, label: Coordinates) -> List[Coordinates]:
#         # Get the neighbors of a vertex
#         return self.adj_list[label]

from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjListGraph(Graph):
    """
    Represents an undirected graph. Please complete the implementations of each method.
    """
    
    def __init__(self):
        # Initialize an empty dictionary to store vertices and their neighbors
        self.adj_list = {}
        # Dictionary to store wall status between vertices
        self.wall_status = {}

    def addVertex(self, label: Coordinates):
     
        # Add a new vertex to the graph
        if label not in self.adj_list:
            self.adj_list.setdefault(label, [])


    def addVertices(self, vertLabels: List[Coordinates]):
        # Add multiple vertices to the graph
        i = 0
        n = len(vertLabels)
        while i < n:
            if vertLabels[i] not in self.adj_list:
                self.adj_list[vertLabels[i]] = []
            i += 1

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
    
        if vert1.isAdjacent(vert2):
        # Add an edge between two vertices
         if vert1 not in self.adj_list or vert2 not in self.adj_list:
            return False

        # Check if the edge already exists
        if vert2 not in self.adj_list[vert1]:
            # Add the edge
            self.adj_list[vert1].append(vert2)
            self.adj_list[vert2].append(vert1)  # Undirected graph
            self.wall_status[(vert1, vert2)] = addWall
            return True

        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        # Update wall status between two vertices
        
        if (vert1, vert2) in self.wall_status:
            self.wall_status[(vert1, vert2)] = wallStatus
            return True
        elif (vert2, vert1) in self.wall_status:
            self.wall_status[(vert2, vert1)] = wallStatus
            return True
        else:
            return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Remove an edge between two vertices
        if vert1 not in self.adj_list or vert2 not in self.adj_list:
            return False
        
        if vert2 in self.adj_list[vert1]:
            self.adj_list[vert1].remove(vert2)
            self.adj_list[vert2].remove(vert1)
            if (vert1, vert2) in self.wall_status:
                del self.wall_status[(vert1, vert2)]
            elif (vert2, vert1) in self.wall_status:
                del self.wall_status[(vert2, vert1)]
            return True
        
        return False
    
    #TestPush
    #Test2

    def hasVertex(self, label: Coordinates) -> bool:
        # Check if a vertex exists in the graph
        return label in self.adj_list

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Check if an edge exists between two vertices
        if vert1 not in self.adj_list or vert2 not in self.adj_list:
            return False
        return vert2 in self.adj_list[vert1]

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Get wall status between two vertices
        if (vert1, vert2) in self.wall_status:
            return self.wall_status[(vert1, vert2)]
        elif (vert2, vert1) in self.wall_status:
            return self.wall_status[(vert2, vert1)]
        else:
            return False  # No wall if not explicitly set

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        # Get the neighbors of a vertex
        return self.adj_list[label]
