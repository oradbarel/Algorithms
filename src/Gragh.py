#A program to get a graph from user, via terminal, and return it as aמ adjacency list.

##### Constants:

QUIT_CHAR = 'q'
YES_CHAR = 'y'
NOT_CHAR = 'n'

##### Classes:

class QuitError(Exception):
    pass

##### Functions:
def getEdge(verts_list: list) -> tuple:
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

def getGraphFromTerminal() -> list:
    n = int(input("Insert number of vertices: "))
    V_list = [i for i in range(1, n+1)]
    print("V is: " + str(V_list))
    G = [[] for i in range(1, n+1)]

    # Wether the graph is directed or not:
    directed = ''
    while(1):
        directed = input("Press 'y' for directed graph or 'n' for undirected graph: ").lower()
        if (directed in [YES_CHAR, NOT_CHAR]):
            break
    directed = True if directed == YES_CHAR else False

    # Get the edges:
    E = []
    print("Now, enter the edges (you may prees 'q' when you want to finish):")
    while(1):
        try:
            (src, dst) = getEdge(V_list)
        except(QuitError):
            break
        e = ((int(src), int(dst)))
        E.append(e)
        print("edge #{0}: {1}.".format(len(E), e))
    print("E is: " + str(E))

    return G

def getGraphFromJson():
    pass

def getGraphFromGUI():
    pass

##### Main Code:

def main():
    getGraphFromTerminal()

if __name__ == "__main__":
    main()