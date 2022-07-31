#A program to get a graph from user, via terminal, and return it as an adjacency list.

import Gragh as gr

##### Constants:

QUIT_CHAR = 'q'
YES_CHAR = 'y'
NOT_CHAR = 'n'

#####=====================================

##### Classes:

class QuitError(Exception):
    def __str__(self) -> str:
        return "Done inserting edges."

#####=====================================

##### Functions:

##### A set of functions to get the graph from the user's terminal:

def getConditionFromTerminal(prompt: str) -> bool:
    cond = ''
    while(1):
        cond = input(prompt).lower()
        if (cond in [YES_CHAR, NOT_CHAR]):
            break
    return (cond == YES_CHAR)

def getIfDirectedFromTerminal() -> bool:
    arg = "Press '{0}' for directed graph or '{1}' for undirected graph: ".format(YES_CHAR, NOT_CHAR)
    return getConditionFromTerminal(arg)

def getIfWeightedFromTerminal() -> bool:
    arg = "Press '{0}' for a weighted graph or '{1}' otherwise: ".format(YES_CHAR, NOT_CHAR)
    return getConditionFromTerminal(arg)

def getIfColoredFromTerminal() -> bool:
    arg = "Press '{0}' for a colored-edges graph or '{1}' otherwise: ".format(YES_CHAR, NOT_CHAR)
    return getConditionFromTerminal(arg)

def getPropertiesFromTerminal() -> tuple[bool, bool, bool]:
    directed = getIfDirectedFromTerminal()
    weighted = getIfWeightedFromTerminal()
    colored = getIfColoredFromTerminal()
    return (directed, weighted, colored)

def getEdgeFromTerminal(verts_list: list, properties: tuple[bool, bool, bool]) -> gr.Edge:
    """Gets an edge from user by the keybord. Returns it as a tuple.

:param verts_list: A list of the vertices.
:type verts_list: list
:param properties: 
:type properties: tuple[bool, bool, bool]
:returns: The edge 
:rtype: DirectedEdge or UndirectedEdge class object.
:raises: QuitError if 'q' has been given as an input.
"""
    n = len(verts_list)
    (directed, weighted, colored) = properties
    (src, dst, weight, color) = (0, 0, gr.DEFAULT_WEIGHT, gr.DEFAULT_COLOR)
    while(1):
        src = input("Enter source vertex: ")
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
        dst = input("Enter destination vertex: ")
        if(dst == QUIT_CHAR):
            raise QuitError
        try:
            dst = int(dst)
            if(dst in verts_list):
                break
        except:
            pass
        print("Please insert an integer between 1 to {0}".format(n))

    while(weighted):
        weight = input("Enter the weight: ")
        if(weight == QUIT_CHAR):
            raise QuitError
        try:
            weight = float(weight)
            break
        except:
            pass
        print("Please insert a number")

    while(colored):
        color = input("Enter the color: ")
        if(color == QUIT_CHAR):
            raise QuitError
        try:
            color = int(color)
            break
        except:
            pass
        print("Please insert an integer")

    return gr.DirectedEdge(src, dst, weight, color) if directed else gr.UndirectedEdge(src, dst, weight, color)

def getGraphFromTerminal() -> tuple[list, list, bool]:
    
    properties  = getPropertiesFromTerminal()
    n = int(input("Insert number of vertices: "))
    V, E = [i for i in range(1, n+1)], []
    print("V is: " + str(V))
    print("Now, enter the edges (you may prees 'q' when you want to finish):")
    while(1):
        try:
            e = getEdgeFromTerminal(V, properties)
        except(QuitError):
            break
        E.append(e)
        print("edge #{0}: {1}.".format(len(E), e))
    print("E is: ", E)

    return (V, E, properties[0])

#####=====================================

##### A set of functions to get the graph from the user's json file:   

def getGraphFromJson():
    pass

def getGraphFromGUI():
    pass

#####=====================================
#####=====================================

##### Main Code:

def main():
    
    (V, E, directed) = getGraphFromTerminal()
    my_graph = gr.DirectedGraph(V, E) if directed else gr.UndirectedGraph(V, E)
    """

    my_gr1 = DirectedGraph([1, 2, 3, 4, 5], [DirectedEdge(1, 2), DirectedEdge(3, 2), DirectedEdge(1, 4)])
    print(my_gr1._adjacency_list)

    my_gr2 = UndirectedGraph([1, 2, 3, 4, 5], [UndirectedEdge(1,2), UndirectedEdge(5,2), UndirectedEdge(4,3)])
    print(my_gr2._adjacency_list)
    print("neighbors of 2:", (my_gr2.getNeighborsOf(2)))

    print(UndirectedEdge(1, 2))"""

if __name__ == "__main__":
    main()