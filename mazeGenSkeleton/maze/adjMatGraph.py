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
            index = len(self.vertices)
            self.vertices[label] = index
            self.adj_matrix[label] = [False] * index  # Initialize row with zeros
        
            # Update existing vertices with new column for the new vertex
            vertex_labels = list(self.vertices.keys())
            vertex_index = 0
            while vertex_index < len(vertex_labels):
                vertex_label = vertex_labels[vertex_index]
                self.adj_matrix[vertex_label].append(False)  # Add new column for the new vertex
                vertex_index += 1
        
            return True
        return False

    def addVertices(self, vertLabels: List[Coordinates]):
        success = all(self.addVertex(label) for label in vertLabels)
        return success
    
    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            index1, index2 = self.vertices[vert1], self.vertices[vert2]
            self.adj_matrix[vert1][index2] = True
            self.adj_matrix[vert2][index1] = True
            if addWall:
                self.adj_matrix[vert1][index2] = 2
                self.adj_matrix[vert2][index1] = 2
            return True
            
        return False





    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
         if vert1 in self.vertices and vert2 in self.vertices:
             v1, v2 = self.vertices[vert1], self.vertices[vert2]
        
             # If wallStatus is True, set the adjacency matrix value to 2 (indicating a wall)
             # Otherwise, set it to False (indicating an edge)
             self.adj_matrix[vert1][v2] = 2 if wallStatus else False 
             self.adj_matrix[vert2][v1] = 2 if wallStatus else False 
        
             return True
    
         return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
          if vert1 in self.vertices and vert2 in self.vertices:
              index1, index2 = self.vertices[vert1], self.vertices[vert2]
        
              # Set the adjacency matrix value to 0 to indicate no edge between the vertices
              self.adj_matrix[vert1][index2] = 0
              self.adj_matrix[vert2][index1] = 0
        
              return True
    
          return False

    def hasVertex(self, label: Coordinates) -> bool:
        return label in self.vertices.keys()


    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            index1, index2 = self.vertices[vert1], self.vertices[vert2]
            for vertex, index in self.vertices.items():
                if index == index1:
                    return self.adj_matrix[vertex][index2]
        return False


    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
      if vert1 in self.vertices and vert2 in self.vertices:
          index1, index2 = self.vertices[vert1], self.vertices[vert2]
          vertices = list(self.vertices.keys())
          i = 0
          while i < len(vertices):
              if i == index1:
                  return self.adj_matrix[vertices[i]][index2] == 2
              i += 1
      return False


    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        if label in self.vertices:
            neighbours = []
            label_pos = self.vertices[label]
            vertices = list(self.vertices.keys())
            pos = 0
            while pos < len(vertices):
                if self.adj_matrix[vertices[pos]][label_pos]:
                    neighbours.append(vertices[pos])
                pos += 1
            return neighbours
        return []
