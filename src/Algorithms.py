import Gragh as gr

def topologicalSort(dag: gr.DirectedGraph) -> list[int]:
    vertices = dag.getVertexDict()
    sources = [key for key, value in vertices.items() if value.getIndegree() == 0] # a queue of sources.
    sorted = {} # return value
    l = 1
    while(vertices):
        v = sources.pop() 
        sorted[v] = l 
        l+=1
        for e in dag.getNeighborsOf(v):
            dst = e.getEdge()[1]
            if(vertices[dst].decrementIndegree() == 0):
                sources.append(dst)
        vertices.pop(v)
    return sorted

my_gr = gr.DirectedGraph([1, 2, 3, 4, 5, 6], [gr.DirectedEdge(3, 1), gr.DirectedEdge(3, 2), gr.DirectedEdge(2, 1), gr.DirectedEdge(6, 4)])
sorted = topologicalSort(my_gr)
print(sorted)