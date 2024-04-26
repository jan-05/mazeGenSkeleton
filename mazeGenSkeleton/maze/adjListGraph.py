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
         # Iterate over both possible combinations of (vert1, vert2) and (vert2, vert1)
         for v1, v2 in [(vert1, vert2), (vert2, vert1)]:
             if (v1, v2) in self.wall_status:
                 # Update the wall status
                 self.wall_status[(v1, v2)] = wallStatus
                 return True  # Return True after updating
         # If no matching key is found, return False
         return False


    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
    # Iterate over both possible combinations of (vert1, vert2) and (vert2, vert1)
            for v1, v2 in [(vert1, vert2), (vert2, vert1)]:
                # Check if the pair exists in self.adj_list
                if v2 in self.adj_list.get(v1, []):
                    # Remove the edge
                    self.adj_list[v1].remove(v2)
                    self.adj_list[v2].remove(v1)
                    # Check and delete the wall status if it exists
                    if (v1, v2) in self.wall_status:
                        del self.wall_status[(v1, v2)]
                    elif (v2, v1) in self.wall_status:
                        del self.wall_status[(v2, v1)]
                    return True  # Return True after removing the edge
            # If no matching pair is found, return False
            return False


    #TestPush
    #Test2

    def hasVertex(self, label: Coordinates) -> bool:
           # Check if a vertex exists in the graph
           for vertex in self.adj_list:
               if vertex == label:
                   return True
           return False


    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Check if an edge exists between two vertices
       
        return vert2 in self.adj_list[vert1]

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
    # Get wall status between two vertices
        wall_status_1 = self.wall_status.get((vert1, vert2), False)
        wall_status_2 = self.wall_status.get((vert2, vert1), False)
        return wall_status_1 or wall_status_2


    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        # Get the neighbors of a vertex
        return self.adj_list[label]
