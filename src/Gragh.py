#A program to get a graph from user, via terminal, and return it as an adjacency list.

##### Constants:

QUIT_CHAR = 'q'
YES_CHAR = 'y'
NOT_CHAR = 'n'

##### Classes:

class QuitError(Exception):
    pass

class Graph:
    """
    Abstract Base class for representing a graph - either directed or undirected.
    """
    def __init__(self, V: list, E: list) -> None:
        self._V = V
        self._E = E
        self._verts_num = len(self._V)
        if(self._verts_num == 0):
            raise ValueError
        self._edges_num = len(self._E)
        self._adjacency_list = self.__makeAdjacencyList__()

    def __makeAdjacencyList__(self) -> list:
            return {i: [] for i in range(1, self._verts_num+1)}
    
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
            raise ValueError("argument must be an integer between 1 to {0}".format(self._verts_num))
        return self._adjacency_list[v]
    
    def isEdgeExists(self, src: int, dst: int):
        """
        Checks if the edge (src, dst) exists in the graph or not.
        Complexity: O(d_out(src)).
        :param src: The source vertice.
        :type src: int.
        :param dst: The destination vertice.
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
            raise ValueError("arguments must be an integer between 1 to {0}".format(self._verts_num))
        src_neighbors = self.getNeighborsOf(src)
        return (dst in src_neighbors)

class DirectedGraph(Graph):

    def __init__(self, V: list, E: list) -> None:
        super().__init__(V, E)

    def __makeAdjacencyList__(self) -> list:
        adjacency_list = super().__makeAdjacencyList__()
        for (src,dst) in self._E:
            adjacency_list[src].append(dst)
        return adjacency_list


class UndirectedGraph(Graph):

    def __init__(self, V: list, E: list) -> None:
        super().__init__(V, E)

    def __makeAdjacencyList__(self) -> list:
        adjacency_list = super().__makeAdjacencyList__()
        for (src,dst) in self._E:
            adjacency_list[src].append(dst)
            adjacency_list[dst].append(src)
        return adjacency_list


##### Functions:

def getIfDirectedFromTerminal() -> bool:
    directed = ''
    while(1):
        directed = input("Press 'y' for directed graph or 'n' for undirected graph: ").lower()
        if (directed in [YES_CHAR, NOT_CHAR]):
            break
    return (directed == YES_CHAR)

def getEdgeFromTerminal(verts_list: list) -> tuple:
    """Gets an edge from user by the keybord. Returns it as a tuple.

:param verts_list: A list of the vertices.
:type verts_list: list
:returns: The edge - (src, dst)
:rtype: tuple
"""
    n = len(verts_list)
    while(1):
        src = input("Enter source vertice: ")
        if(src == QUIT_CHAR):
            raise QuitError
        try:
            src = int(src)
            if(src in verts_list):
                break
        except:
            pass
        print("Please insert an integer between 1 to {0}".format(n))

    while(1):
        dst = input("Enter destination vertice: ")
        if(dst == QUIT_CHAR):
            raise QuitError
        try:
            dst = int(dst)
            if(dst in verts_list):
                break
        except:
            pass
        print("Please insert an integer between 1 to {0}".format(n))
    return (src, dst)

def getGraphFromTerminal() -> tuple:
    
    directed = getIfDirectedFromTerminal()

    n = int(input("Insert number of vertices: "))
    V = [i for i in range(1, n+1)]
    print("V is: " + str(V))

    E = []
    print("Now, enter the edges (you may prees 'q' when you want to finish):")
    while(1):
        try:
            (src, dst) = getEdgeFromTerminal(V)
        except(QuitError):
            break
        e = ((int(src), int(dst)))
        E.append(e)
        print("edge #{0}: {1}.".format(len(E), e))
    print("E is: " + str(E))

    return (V, E, directed)

def getGraphFromJson():
    pass

def getGraphFromGUI():
    pass

##### Main Code:

def main():
    """
    (V, E, directed) = getGraphFromTerminal()
    my_graph = DirectedGraph(V, E) if directed else UndirectedGraph(V, E)
    # """

    my_gr1 = DirectedGraph([1, 2, 3, 4, 5], [(1,2), (5,2), (4,3)])
    print(my_gr1._adjacency_list)
    my_gr2 = UndirectedGraph([1, 2, 3, 4, 5], [(1,2), (5,2), (4,3)])
    print(my_gr2._adjacency_list)
    print("neighbors of 2: " + str(my_gr2.getNeighborsOf(2)))



if __name__ == "__main__":
    main()