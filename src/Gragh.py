#A program to get a graph from user, via terminal, and return it as an adjacency list.

##### Constants:


DEFAULT_WEIGHT = 1
DEFAULT_COLOR = None

#####=====================================


class Vertex:
    """
    Class for representing a vertex in graph, for future algorithms.
    """
    def __init__(self, key, color = None) -> None:
        self._key = key
        self._color = color
    
    def getKey(self):
        return self._key

    def getColor(self):
        return self._color

    def setColor(self, color) -> None:
        self._color = color

class Edge:
    """
    Base class for representing an egde.
    You should one of its subclasses - `DirectedEdge` or `UndirectedEdge`.
    """
    def __init__(self, src: int, dst: int, weight: float = DEFAULT_WEIGHT, color = DEFAULT_COLOR) -> None:
        self._src = src
        self._dst = dst
        self._weight = weight
        self._color = color

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return '({0}, {1}). weight = {2}. color = {3}'.format(self._src, self._dst, self._weight, self._color)

    def getSource(self) -> int:
        return self._src

    def getDestination(self) -> int:
        return self._dst

    def getEdges(self) -> tuple[int, int]:
        return (self._src, self._dst)

    def getWeight(self):
        return self._weight

    def setWeight(self, weight) -> None:
        self._weight = weight

    def getColor(self):
        return self._color

    def setColor(self, color) -> None:
        self._color = color

class DirectedEdge(Edge):
    def __init__(self, src: int, dst: int, weight: float = DEFAULT_WEIGHT, color=DEFAULT_COLOR) -> None:
        super().__init__(src, dst, weight, color)

    def __str__(self) -> str:
        return super().__str__()

    def getEdges(self) -> tuple[int, int]:
        return super().getEdges()

class UndirectedEdge(Edge):
    def __init__(self, src: int, dst: int, weight: float = DEFAULT_WEIGHT, color=DEFAULT_COLOR) -> None:
        super().__init__(src, dst, weight, color)

    def __str__(self) -> str:
        return super().__str__().replace("(", "{").replace(")", "}")

    def getEdges(self) -> set[int]:
        return set((super().getEdges()))

class Graph:
    """
    Base class for representing a graph - either directed or undirected.
    You should one of its subclasses - `DirectedGraph` or `UndirectedGraph`.
    """
    def __init__(self, V: list, E: list[Edge] = []) -> None:
        self._V = V
        self._E = E
        if(len(self._V) == 0):
            raise ValueError
        self._adjacency_list = self.__makeAdjacencyList__()

    def __makeAdjacencyList__(self) -> dict:
            return {i: [] for i in range(1, len(self._V)+1)}
    
    def getVertices(self):
        return self._V

    def getEdges(self):
        return self._E

    def getAdjacencyList(self) -> dict:
        return self._adjacency_list

    def getNumOfVertices(self):
        return len(self._V)

    def getNumOfEdges(self):
        return len(self._E)

    def getNeighborsOf(self, v: int) -> list:
        try:
            v = int(v)
        except:
            raise TypeError("argument must be an integer")            
        if(v not in self._V):
            raise ValueError("argument must be an integer between 1 to {0}".format(len(self._V)))
        return self._adjacency_list[v]
    
    def addVertex(self, v: int) -> None:
        """
        Function for algorithms uses (not for user).
        """
        try:
            v = int(v)
        except:
            raise TypeError("argument must be an integer")            
        if(v in self._V):
            raise ValueError("vertex {0} already exists".format(len(self._V)))
        self._V.append(v)
        self._adjacency_list[v] = []

    def isEdgeExists(self, src: int, dst: int):
        """
        Checks if the edge (src, dst) exists in the graph or not.
        Complexity: O(d_out(src)).
        :param src: The source vertex.
        :type src: int.
        :param dst: The destination vertex.
        :type dst: int.
        :returns: True - if exists, False if does not exist
        :rtype: bool
        :raises TypeError: If src or dst are not of type int or can not be casted to int.
        :raises ValueError: If src or dst are not integers in [1, |V|].
        """
        try:
            src, dst = int(src), int(dst)
        except:
            raise TypeError("arguments must be an integer")            
        if((src not in self._V) or (dst not in self._V)):
            raise ValueError("arguments must be an integer between 1 to {0}".format(len(self._V)))
        src_neighbors = self.getNeighborsOf(src)
        return (dst in src_neighbors)

class DirectedGraph(Graph):

    def __init__(self, V: list, E: list) -> None:
        super().__init__(V, E)

    def __makeAdjacencyList__(self) -> dict:
        adjacency_list = super().__makeAdjacencyList__()
        for edge in self._E:
            src = edge.getSource()
            adjacency_list[src].append(edge)
        return adjacency_list

class UndirectedGraph(Graph):

    def __init__(self, V: list, E: list) -> None:
        super().__init__(V, E)

    def __makeAdjacencyList__(self) -> dict:
        adjacency_list = super().__makeAdjacencyList__()
        for edge in self._E:
            (v1, v2) = tuple(edge.getEdges())
            adjacency_list[v1].append(edge)
            adjacency_list[v2].append(edge)
        return adjacency_list

#####=====================================


